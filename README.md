# Litecoin-test

## Question 1

Basic Litecoin Dockerfile has been taken from this [repository](https://github.com/uphold/docker-litecoin-core/tree/master/0.18)

### Checksum verification

Checksum verification has been already setup. Comment has been added for the checksum verification.

### Security Scan using [Anchore](https://anchore.com/blog/inline-scanning-with-anchore-engine/)

As a tool, Anchore has been used for docker image scanning. An inline scanning with anchore has been performed.

After building the Dockerfile using:
```
docker build -t litecoin:0.18.1 .
```

Time for scanning:

curl -s https://ci-tools.anchore.io/inline_scan-v0.6.0 | bash -s -- -f -d Dockerfile -b .anchore-policy.json litecoin:0.18.1

Scan result can be found below:

![Scan](scan.png)

## Question 2

In order to deploy the stack as a statefulset:

### Environment setup 

first setup a quick Kubernetes environement using [Minikube](https://minikube.sigs.k8s.io/docs/start/)
```
minikube start
```
### Docker image build 
After installing Minikube, re-build the Docker image inside Minikube VM so it can be pulled from Kubernetes when deploying the statefulset.
```
docker build -t litecoin:0.18.1 .
```

### Configure & Deploy the StatefulSet

The statefulset has been configured in order to deploy the pod containing the container instance of the litecoin docker image as well as mounting/creating the PVC using volumeClaimTemplate & VolumeMount.
```
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: litecoin
        image: litecoin:0.18.1
        ports:
        - containerPort: 9332
          name: litecoin
        volumeMounts:
        - name: litecoin
          mountPath: /home/litecoin/.litecoin
  volumeClaimTemplates:
  - metadata:
      name: litecoin
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi

```

For full configuration, please check this [link](https://github.com/iliasnaamane/Litecoin-test/blob/master/2/ss.yml).

### Verification

Verify that the statefulset is correctly running & ready.
![SS](ss.png)

Verify that the pod deployed by the statefulset is correctly running & ready.
![Pod](pod.png)

Verify that the PVC & PV has been correctly created and mounted.
![PV](pv.png)



