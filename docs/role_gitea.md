---
title: Gitea
summary: Ansible Role to install Gitea

authors:
  - Kamesh Sampath<kamesh.sampath@hotmail.com>
date: 2021-12-01
---

This role helps in installing and configuring [Gitea](https://gitea.io/en/stable/) the Kubernetes cluster.

## Requirements

Access to Kubernetes cluster,

---8<--- "includes/minikube_cluster.md"

## Variables

| Name  | Description | Default
| ----------- | ----------- | ---
| kubernetes_spices_gitea_k8s_context | The Kubernetes context where Gitea will be installed. The playbook will fail if this is not set. |
| kubernetes_spices_gitea_namespace| The namespace to install Gitea | gitea
| kubernetes_spices_gitea_cli_version| The gitea cli version | 1.15.6

## Example Playbook

```yaml
---8<--- "examples/gitea.yml"
```

!!! important
    - Based on the above example the `kubernetes_spices_gitea_k8s_context` should be set to `mgmt`, the context which is created by minikube
    - The gitea password will be generated and stored in the `{{ work_dir }}/gitea.password` file. The default admin username is `gitea`

The playbook installs a proxy in the namespace where Gitea is installed to allow the service to be accessed from the host machine. To get your gitea url run,

```bash
GITEA_URL=
gitea-$(kubectl -n gitea gateway-proxy -ojsonpath='{.status.loadBalancer.ingress[*].ip}').nip.io"
```
