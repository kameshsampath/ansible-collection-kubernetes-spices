#!/bin/bash
set -e
set -o pipefail

ISTIO_INGRESS_NS=${ISTIO_INGRESS_NS:-istio-ingress}

###########################################
# Deploy Ingress Gateway
###########################################

NS=$(kubectl get namespace "$ISTIO_INGRESS_NS" --ignore-not-found);
if [[ "$NS" ]]; then
  echo "Skipping creation of namespace $ISTIO_INGRESS_NS - already exists";
else
  echo "Creating namespace $ISTIO_INGRESS_NS";
  kubectl create namespace "$ISTIO_INGRESS_NS";
fi;

echo "$ISTIO_GATEWAY_MANIFEST" > /tmp/istio-ingress-gateway.yaml
istioctl install -y -n "$ISTIO_INGRESS_NS" \
  --revision "$ISTIO_REVISION" \
  -f /tmp/istio-ingress-gateway.yaml
