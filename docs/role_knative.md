---
title: Knative
summary: Ansible Role to install Knative

authors:
  - Kamesh Sampath<kamesh.sampath@hotmail.com>
date: 2021-12-01
---

This role helps in installing and configuring [Knative](https://knative.dev) Serving and Eventing on to the Kubernetes cluster.

## Requirements

Access to Kubernetes cluster,

---8<--- "includes/minikube_cluster.md"

## Variables

| Name  | Description | Default
| ----------- | ----------- | ---
| kubernetes_spices_gitea_k8s_context | The Kubernetes context where Knative will be installed. The playbook will fail if this is not set. |
| kubernetes_spices_knative_serving_version| The Knative Serving version to use| v1.0.0
| kubernetes_spices_knative_eventing_version| The Knative Eventing version to use | v1.0.0
| kubernetes_spices_registries_skip_tag_resolving| The list of registry urls which need to be ignored for tag resolving | example.com,example.org,test.com,test.org,ko.local,dev.local,localhost:5000,kind-registry.local:5000

## Example Playbook

```yaml
---8<--- "examples/knative.yml"
```

!!! important
    - Based on the above example the `kubernetes_spices_knative_k8s_context` should be set to `mgmt`, the context which is created by minikube.
