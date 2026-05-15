## Devops Build and Deployment Platform

### Project Overview

This project is built to show the deployment of a simple flask application using
docker and kubernetes. Application is built on a Vagrant based virtual machine.
It mimics the end to end deployment of the application like production style
workflow without using cloud infrastructure.

Flow:
- A virtual machine is spinup using Vagrant
- A simple flask application is created and 3 endpoints are created to expose the application.
- Application is containerized using docker and deployed into k3s cluster
- Application can be accessed using curl.

### Architecture

MAC OS
   |
Vagrant
   |
Ubuntu VM
   |
Docker
   |
Kubernetes
   |
Flask Application

### Technologies and Tools used

- Vagrant
- VMWare Fusion
- Vagrant VMWare Utility
- Docker
- Kubernetes
- Git
- GitHub

### Prequisites

Below tools has to be installed before running the project:
- VMWare Fusion
- Vagrant VMWare Utility
- Vagrant

### Setup Instructions

#### Step 1: Clone Github repository

```bash
git clone git@github.com:capricorn1-tech/devops_project_rhombus.git
```
Above command clones the git repository

#### Step 2: Start the VM
```bash
vagrant up
vagrant ssh
```
Above commands help to build the virtual name using the configuration provided in
the Vagrantfile, vagrant ssh command logs you into vagrant machine

#### Step 3: Docker 
```bash
docker build -f docker/Dockerfile -t flask-app:v1
docker run -d -p 5000:5000 flask-app:v1
```
Above commands builds the docker image and creates the docker container.

#### Step 4: Kubernetes
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```
Above commands apply the kubernetes manifests and create the application container.

#### Step 5: Accessing the application

##### After Docker deployment
```bash
curl http://localhost:5000/ping
curl http://localhost:5000/system-info
curl http://localhost:5000/home
```

##### After Kubernetes deployment
As the application is exposed using NodePort, it is accessed as follows:
```bash
curl http://localhost:30080/ping
curl http://localhost:30080/system-info
curl http://localhost:30080/home
``` 

 
