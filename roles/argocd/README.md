Role Name
=========

Role to install [Argocd](https://argo-cd.readthedocs.io/en/stable/)

Role Variables
--------------

- `kubernetes_spices_argocd_k8s_context` - the Kubernetes context to install Argocd
- `kubernetes_spices_argocd_namespace` - namespace to install argocd, defaults `argocd`
- `kubernetes_spices_argocd_version` - argocd cli version, defaults `2.1.6`

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GPLv3
