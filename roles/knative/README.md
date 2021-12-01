Role Name
=========

Role to install [Knative](https://knative.dev)

Role Variables
--------------

- `kubernetes_spices_knative_k8s_context` - the Kubernetes context to install Knative
- `kubernetes_spices_knative_eventing_version`: the Knative Eventing version to install, defaults to `v1.0.0`
- `kubernetes_spices_knative_serving_version`: the Knative Serving version to install, defaults to `v1.0.0`
- `kubernetes_spices_registries_skip_tag_resolving`: List of repositories to skip resolving tags,
    - example.com
    - example.org
    - test.com
    - test.org
    - ko.local
    - dev.local
    - localhost:5000
    - kind-registry.local:5000

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GPLv3
