Gitea
=========

Role to install [istio](https://istio.io)

Role Variables
--------------

- `kubernetes_spices_istio_namespace`: The namespace to install Istio. Defaults `istio-system`.
- `kubernetes_spices_istio_gateways_namespace`: The namespace to install Istio Gateweays. Default `istio-gateways`
- `kubernetes_spices_istiod_helm_values_files`: The Istio Discovery helm chart value files.
- `kubernetes_spices_istiogw_helm_values_files`: The Istio Gateways helm chart value files.
- `istio_clusters` - Istio clusters is a dictionary that describes where to install Istio 

```yaml
istio_clusters:
  cluster1:
    version: 1.12.1
    install: yes
    k8s_context: cluster1
```

!!!important
    The role supports only Istio v1.12.x and above as it uses the Istio Helm Charts to install Istio. 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GPLv3
