
# Docker & Kubernetes Cloud Deployment Workshop

This hands-on project is designed to help students understand how to containerize an app, orchestrate it using Kubernetes, and deploy it locally or in the cloud.

## Project Structure

```
docker-k8s-cloud-deploy/
├── 1-docker-basics/           # Dockerfile + simple Flask app
├── 2-docker-compose/          # Docker Compose with volume
├── 3-kubernetes-intro/        # Kubernetes deployment + service YAML
├── 4-cloud-hosting/           # Guides for Minikube and Cloud deploy
├── shared/                    # Shared assets (env files, diagrams)
└── README.md                  # You're here
```

## Learning Goals

- Understand what Docker is and why we use containers
- Use Docker Compose to manage multi-service projects with persistent data
- Deploy to Kubernetes using kubectl and YAML files
- Understand NodePort services, container orchestration, and cloud deployment flow

## SESSION 1: Docker Basics

### App: A simple Flask "Hello World"

### Build and Run

```bash
cd 1-docker-basics
docker build -t docker-basics-app .
docker run -p 5000:5000 docker-basics-app
```

Open browser: http://localhost:5000

### Stop

```bash
Ctrl + C
```

Or stop with:

```powershell
docker ps -q | ForEach-Object { docker stop $_ }
```

## SESSION 2: Docker Compose + Volumes

### App: Flask app logs each visit into a file

### Run

```bash
cd ../2-docker-compose
docker-compose up --build
```

Check: http://localhost:5000

### Check Volume Data

```bash
cat volume_data/visit.txt
```

### Stop

```bash
Ctrl + C
docker-compose down
```

## SESSION 3: Kubernetes Deployment

### App: Same Flask app as container, deployed with Kubernetes

### Step 1: Push to Docker Hub

```bash
docker tag docker-basics-app yourdockerhubusername/flask-app
docker push yourdockerhubusername/flask-app
```

Replace `yourdockerhubusername` with your Docker Hub username.

### Step 2: Update Image in YAML

Edit `3-kubernetes-intro/k8s-deployment.yaml`:

```yaml
image: yourdockerhubusername/flask-app
```

### Step 3: Apply to Kubernetes

```bash
cd ../3-kubernetes-intro
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
```

### Access the App

```bash
kubectl get service flask-service
```

Find the NodePort (e.g. 30036) and visit:

```
http://localhost:30036
```

### Cleanup

```bash
kubectl delete -f k8s-deployment.yaml
kubectl delete -f k8s-service.yaml
```

(Optional) Force-remove containers:

```bash
docker ps
docker rm -f <container-id>
```

## SESSION 4: Optional Cloud / Minikube

See:

- 4-cloud-hosting/minikube-guide.md
- 4-cloud-hosting/cloud-deploy.md

## Architecture Diagram

```
Developer → Container → Orchestrator (Kubernetes) → Cloud
```
