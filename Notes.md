# Working Notes

```bash
docker build -t ndhanase927/flask-backend:1.0.0 -f Dockerfile.backend . 
docker push ndhanase927/flask-backend:1.0.0
```

```bash
kubectl apply -f backend-deployment.yaml 
kubectl apply -f backend-service.yaml
```

```bash
docker build -t ndhanase927/flask-load-balancer:1.0.0 -f Dockerfile.loadbalancer .
docker push ndhanase927/flask-load-balancer:1.0.0
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

```bash
ssh -L 8888:192.168.49.2:30080 team12@128.2.205.130
```

`http://localhost:8888/` after tunel forwarding

```bash
ab -n 1000 -c 50 "http://192.168.49.2:30080/?user_id=Alice"
```