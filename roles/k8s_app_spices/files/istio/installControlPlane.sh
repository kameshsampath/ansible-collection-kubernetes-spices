#!/bin/bash
set -e
set -o pipefail 

ISTIO_NS=${ISTIO_NS:-istio-system}

###########################################
# Deploy Control Plane
###########################################

echo "Appling Istio Revision: $ISTIO_REVISION"

NS=$(kubectl get namespace "$ISTIO_NS" --ignore-not-found);
if [[ "$NS" ]]; then
  echo "Skipping creation of namespace $ISTIO_NS - already exists";
else
  echo "Creating namespace $ISTIO_NS";
  kubectl create namespace "$ISTIO_NS";
fi;

SVC=$(kubectl get svc istiod -n "$ISTIO_NS" --ignore-not-found);
if [[ "$SVC" ]]; then
  echo "Skipping creation of service istiod - already exists";
else
  echo "Creating service istiod";
  echo "$ISTIOD_SERVICE_MANIFEST" > /tmp/istiod-service.yaml
  kubectl create -n "$ISTIO_NS" -f /tmp/istiod-service.yaml
fi;

echo "$CONTROL_PLANE_MANIFEST" > /tmp/istio-control-plane.yaml
istioctl install -y -n "$ISTIO_NS" --revision "$ISTIO_REVISION" \
  -f /tmp/istio-control-plane.yaml

rm -f /tmp/istiod-service.yaml
rm -f /tmp/istio-control-plane.yaml