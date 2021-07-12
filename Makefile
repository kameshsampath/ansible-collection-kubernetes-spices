CURRENT_DIR = $(shell pwd)

BUILDER_EE_CONTEXT=builder-ee
BUILDER_EE_FILE=$(CURRENT_DIR)/builder-ee/execution-environment.yml
CONTAINER_RUNTIME=docker
ANSIBLE_RUNNER_IMAGE=quay.io/kameshsampath/kubernetes-spices-ansible-runner

ANSIBLE_BUILDER := poetry run ansible-builder

VERSION=`cat version.txt`
COLLECTION_FQN=kameshsampath.kubernetes_spices
TEST_ARGS ?= ""
PYTHON_VERSION ?= `python -c 'import platform; print("{0}.{1}".format(platform.python_version_tuple()[0], platform.python_version_tuple()[1]))'`

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
	poetry export -o $@

builder-ee/requirements.txt:	requirements.txt
	cp $(CURRENT_DIR)/requirements.txt $@
	
.PHONY:
image:	builder-ee/requirements.txt
	$(ANSIBLE_BUILDER) build --file $(BUILDER_EE_FILE) \
	--context $(CURRENT_DIR)/$(BUILDER_EE_CONTEXT) \
	--tag $(ANSIBLE_RUNNER_IMAGE) \
	--container-runtime $(CONTAINER_RUNTIME)

.PHONY:	push
push:	image
	@$(CONTAINER_RUNTIME) push $(ANSIBLE_RUNNER_IMAGE)