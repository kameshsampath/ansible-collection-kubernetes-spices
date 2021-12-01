---
title: Tektoncd
summary: Ansible Role to install Tektoncd

authors:
  - Kamesh Sampath<kamesh.sampath@hotmail.com>
date: 2021-12-01
---

This role helps in installing and configuring [Tektoncd](https://tekton.dev) on to the Kubernetes cluster.

## Requirements

Access to Kubernetes cluster,

---8<--- "includes/minikube_cluster.md"

## Variables

| Name  | Description | Default
| ----------- | ----------- | ---
| kubernetes_spices_tektoncd_k8s_context | The Kubernetes context where Tektoncd will be installed. The playbook will fail if this is not set. |
| kubernetes_spices_tektoncd_pipelines_version| The Tekton pipelines version to use| v0.29.0
| kubernetes_spices_tektoncd_triggers_version| The Tekton triggers version to use | v0.16.0
| kubernetes_spices_tkn_cli_version| The `tkn` cli version | v0.21.0

## Example Playbook

```yaml
---8<--- "examples/knative.yml"
```

!!! important
    - Based on the above example the `kubernetes_spices_tektoncd_k8s_context` should be set to `mgmt`, the context which is created by minikube.
