# Minikube Deployment Guide

1. Start Minikube:
```bash
minikube start
```

2. Apply Kubernetes manifests:
```bash
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
```

3. Access the service:
```bash
minikube service flask-service
```
