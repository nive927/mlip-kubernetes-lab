# Working Notes

```bash
docker build -t ndhanase927/mlops-flask-app:1.0.0 -f Dockerfile.backend . 
docker push ndhanase927/mlops-flask-app:1.0.0
```

```bash
kubectl apply -f backend-deployment.yaml 
kubectl apply -f backend-service.yaml
```

```bash
docker build -t ndhanase927/load-balancer:1.0.0 -f Dockerfile.loadbalancer .
docker push ndhanase927/load-balancer:1.0.0
```

```bash
kubectl apply -f loadbalancer-deployment.yaml 
kubectl apply -f loadbalancer-service.yaml
```

```bash
minikube ip # 192.168.49.2
```

```bash
curl "http://192.168.49.2:30080/?user_id=Alice"
```