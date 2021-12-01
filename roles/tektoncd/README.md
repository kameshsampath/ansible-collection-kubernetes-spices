Role Name
=========

Role to install [Tektoncd](https://tekton.dev)

Role Variables
--------------

- `kubernetes_spices_tektoncd_k8s_context`  - the Kubernetes context to install Knative
- `kubernetes_spices_tektoncd_pipelines_version` - tektoncd pipelines version, defaults to `v0.29.0`
- `kubernetes_spices_tektoncd_triggers_version` - tektoncd triggers version, defaults to  `v0.16.0`
- `kubernetes_spices_tkn_cli_version` - tektoncd cli version, defaults to 0.21.0

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GPLv3
