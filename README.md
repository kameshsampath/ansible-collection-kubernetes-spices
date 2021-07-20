# Ansible Collection for Spicing Kubernetes Cluster with Apps

[![Ansible Galaxy Collection](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/release-collection.yml/badge.svg)](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/release-collection.yml) [![Ansible Runner](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/release.yml/badge.svg)](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/release.yml) [![Documentation](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/site.yml/badge.svg)](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/site.yml) [![Dev Ansible EE Image](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/dev-image.yaml/badge.svg)](https://github.com/kameshsampath/kubernetes_spices/actions/workflows/dev-image.yaml) 

The [Ansible collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) that can help in setting up Kubernetes cluster such as [KinD](https://kind.sigs.k8s.io) or deploy components to existing Kubernetes cluster.

Check out the HTML documentation https://kameshsampath.github.io/kubernetes_spices

## Requirements

[Docker Desktop](https://www.docker.com/products/docker-desktop) or Docker for Linux

## Build Locally


### Requirements

* [Python Poetry](https://python-poetry.org/)

* [Docker Desktop](https://www.docker.com/products/docker-desktop) or Docker for Linux

* [Ansible](https://ansible.com) >= v2.9.10

```shell
poetry install
poetry shell
ansible-galaxy role install -r requirements.yml
ansible-galaxy collection install -r requirements.yml
```

__NOTE__: For Windows its recommended to use Windows Subsystem for Linux (WSL)

## License

[GPL v3](https://github.com/kameshsampath/kameshsampath.kubernetes_spices/tree/master/LICENSE)

## Author Information

[Kamesh Sampath](mailto:kamesh.sampath@hotmail.com)

## Issues

[Issues](https://github.com/kameshsampath/kameshsampath.kubernetes_spices/issues)
