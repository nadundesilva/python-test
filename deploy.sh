#!/bin/bash

IMAGE="nadunrds/python-test:latest"

docker rmi "${IMAGE}"
docker build -t "${IMAGE}" .
docker push "${IMAGE}"

kubectl delete --wait -f ./k8s/
kubectl apply -f ./k8s/
