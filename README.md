# Ansible role for Spicing Kubernetes Cluster with Apps

Ansible to create [KinD](https://kind.sigs.k8s.io) cluster with `ipv6` or `ipv4` or `dual` stack.

The role can also be used to install and configure:

- [x] Default [Istio](https://istio.io)

- [x] [Knative](https://knative.dev), both Serving and Eventing

- [x] [Tekton](https://tekton.dev)

## Requirements

- [Python Poetry](https://python-poetry.org/)

- [Docker Desktop](https://www.docker.com/products/docker-desktop) or Docker for Linux

- [Ansible](https://ansible.com) >= v2.9.10

__TODO: update with collection install__

```shell
poetry install
poetry shell
ansible-galaxy role install -r requirements.yml
ansible-galaxy collection install -r requirements.yml
```

__NOTE__: For Windows its recommended to use Windows Subsystem for Linux (WSL)

## Role Variables

| Variable Name| Description | Default |
|--|--|--|
| kubernetes_cluster_type | The Kubernetes Cluster Type minikube or kind or custom | minikube |
| k8s_cluster_ip | The Kubernetes Cluster IP | Auto configured for minikube or KinD |
| deploy_knative | Deploy Knative | False |
| knative_version | The Knative version | v0.16.0 |
| knative_serving_version | The Knative Serving version | v0.16.0 |
| knative_eventing_version | The Knative Eventing version | v0.16.0 |
| deploy_ingress | Deploy Ingress | True |
| ingress_namespace | The namespace for Contour Ingress | contour-system |
| ingress_namespace | The namespace for Contour Ingress | contour-system |
| ingress_manifest  | The Contour Ingress manifest file  | [Project Contour](https://projectcontour.io/quickstart/contour.yaml) |
| deploy_tektoncd | Deploy Tektoncd | False |
| tektoncd_pipelines_version | Tektoncd Pipelines Version | v0.11.3 |
| tektoncd_triggers_version | Tektoncd Triggers Version | v0.4.0 |
| deploy_argocd | Deploy [Argo CD](https://argoproj.github.io/) | False |
| argocd_namespace | Argo CD namespace | argocd |
| argocd_version | Argo CD version to use | v1.6.2 |

## Example Playbooks

The [examples](https://github.com/kameshsampath/kameshsampath.kubernetes_spices/tree/master/examples) directory has various playbook examples to get started using this role

## License

[GPL v3](https://github.com/kameshsampath/kameshsampath.kubernetes_spices/tree/master/LICENSE)

## Author Information

[Kamesh Sampath](mailto:kamesh.sampath@hotmail.com)

## Issues

[Issues](https://github.com/kameshsampath/kameshsampath.kubernetes_spices/issues)
