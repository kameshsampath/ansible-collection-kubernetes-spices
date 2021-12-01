---
title: Argocd
summary: Ansible Role to install Argocd
authors:
  - Kamesh Sampath<kamesh.sampath@hotmail.com>
date: 2021-12-01
---

This role helps in installing and configuring [Argocd](https://argo-cd.readthedocs.io/en/stable/) the Kubernetes cluster.

## Requirements

Access to Kubernetes cluster,

---8<--- "includes/minikube_cluster.md"

## Variables

| Name  | Description | Default
| ----------- | ----------- | ---
| kubernetes_spices_argocd_k8s_context | The Kubernetes context where Argcod will be installed. The playbook will fail if this is not set. |
| kubernetes_spices_argocd_namespace| The namespace to install Argocd | argocd
| kubernetes_spices_argocd_version| The argocd version to be used | 2.1.6

## Example Playbook

```yaml
---8<--- "examples/argocd.yml"
```

!!! important
    - Based on the above example the `kubernetes_spices_argocd_k8s_context` should be set to `mgmt`, the context which is created by minikube
    - The default credentials to access argocd will be `admin/password`
