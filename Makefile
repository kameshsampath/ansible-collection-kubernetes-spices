CURRENT_DIR = $(shell pwd)
POETRY_COMMAND := $(shell which poetry)

BUILDER_EE_CONTEXT=builder-ee
BUILDER_EE_FILE=$(CURRENT_DIR)/builder-ee/execution-environment.yml
CONTAINER_RUNTIME=docker
ANSIBLE_RUNNER_IMAGE=ghcr.io/kameshsampath/kubernetes-spices-ansible-runner

ANSIBLE_BUILDER := $(shell $(POETRY_COMMAND) run ansible-builder)

TEST_ARGS ?= ""
PYTHON_VERSION ?= `python -c 'import platform; print("{0}.{1}".format(platform.python_version_tuple()[0], platform.python_version_tuple()[1]))'`

ENV_FILE := $(CURRENT_DIR)/.envrc

GALAXY_VERSION := $(shell yq eval '.version' $(CURRENT_DIR)/galaxy.yml)
VERSION := $(GALAXY_VERSION)
RELEASE_ARTIFACT := "$(DIST_DIR)/$(COLLECTION_FQN)-$(GALAXY_VERSION).tar.gz"

shell-env:
	@$(POETRY_COMMAND) install

clean:
	rm -f kameshsampath-kubernetes_spices-${VERSION}.tar.gz
	rm -rf ansible_collections
	rm -rf tests/output

build: clean
	ansible-galaxy collection build

test-sanity:
	ansible-test sanity --docker -v --color --python $(PYTHON_VERSION) $(?TEST_ARGS)

test-integration:
	ansible-test integration --docker -v --color --retry-on-error --python $(PYTHON_VERSION) --continue-on-error --diff --coverage $(?TEST_ARGS)

test-molecule:
	molecule test

test-unit:
	ansible-test units --docker -v --color --python $(PYTHON_VERSION) $(?TEST_ARGS)

requirements.txt:
	poetry export --without-hases -o $@

builder-ee/requirements.txt:	requirements.txt
	cp $(CURRENT_DIR)/requirements.txt $@
	
.PHONY:
container-file:  
	$(ANSIBLE_BUILDER) create \
  --file  $(CURRENT_DIR)/$(BUILDER_EE_CONTEXT)/execution-environment.yml \
	--context $(CURRENT_DIR)/$(BUILDER_EE_CONTEXT) \
	--output-filename Dockerfile

.PHONY:
image-build:
	$(ANSIBLE_BUILDER) build --file $(BUILDER_EE_FILE) \
	--context $(CURRENT_DIR)/$(BUILDER_EE_CONTEXT) \
	--tag $(ANSIBLE_RUNNER_IMAGE) \
	--container-runtime $(CONTAINER_RUNTIME)

.PHONY:	push
push:	image-build
	@$(CONTAINER_RUNTIME) push $(ANSIBLE_RUNNER_IMAGE)

build_collection:
	direnv allow $(ENV_FILE)
	@$(POETRY_COMMAND) run ansible-galaxy collection build \
	  --out $(DIST_DIR) \
		--force \
	  $(EXTRA_ARGS)

publish_collection:
	direnv allow $(ENV_FILE)
	@$(POETRY_COMMAND) run ansible-galaxy collection publish \
	  $(RELEASE_ARTIFACT) \
		--server $(ANSIBLE_GALAXY_SERVER_RELEASE_SERVER) \
		--token $(ANSIBLE_GALAXY_SERVER_RELEASE_GALAXY_TOKEN) \
		$(EXTRA_ARGS)