# natali-weather-app
Python based application to check the weather apis.

### Docker Build
```
docker build -t natallie/weather-app:latest .
```

### Deployment in kubernetes
Kubernetes manifest files are located in `deployment` folder
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

### Application endpoint
```
http://<loadbalancer-ip-address>:80
```
