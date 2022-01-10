---
title: Argocd
summary: Ansible Role to install Istio
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
| kubernetes_spices_argocd_helm_secerts_plugin | Use helm secrets plugin with argocd applications | false

## Example Playbook

```yaml
---8<--- "examples/argocd.yml"
```

!!! important
    - Based on the above example the `kubernetes_spices_argocd_k8s_context` should be set to `mgmt`, the context which is created by minikube
    - The default credentials to access argocd will be `admin/password`

## Using helm secrets plugin

To use helm secrets plugin with Argocd applications, enable the plugin configuration by adding enable the flag `kubernetes_spices_argocd_helm_secerts_plugin` to `true`.

Lets take an example of [sops](https://github.com/mozilla/sops) and [age](https://github.com/FiloSottile/age),

## Create age key

```shell
age-keygen -o key.txt
```

Move the `key.txt` to secure place, preferably `$HOME/.ssh`. Assuming you moved it to `$HOME/.ssh`, lets set that as local environment variables for convinience:

```bash
export SOPS_AGE_KEY_FILE="$HOME/.ssh/key.txt"
```

Also note and export the **publickey** in the `$SOPS_AGE_KEY_FILE` as `$SOPS_AGE_RECIPIENTS`

```bash
export SOPS_AGE_RECIPIENTS=$(cat $SOPS_AGE_KEY_FILE  | awk 'NR==2{ print $4}')
```

Ensure the sops configration `.sops.yml` is updated with your *age* publickey,

```shell
yq eval '.creation_rules[0].age |= strenv(SOPS_AGE_RECIPIENTS)' .sops.yml 
```

We need to make the age key to be available to the Argocd repo server so that it can decrypt the secrets,

```shell
kubectl create ns argocd
```

```shell
kubectl create secret generic helm-secrets-private-keys \
  --namespace=argocd \
  --from-file=key.txt="$SOPS_AGE_KEY_FILE"
```

Now you an use the same play to deploy Argocd with helm secrets enabled,

```yaml
---8<--- "examples/argocd.yml"
```

You can check the [example project](https://github.com/kameshsampath/helm-secret-demo) to deploy Keycloak using helm secrets plugin enabled with Argocd.
