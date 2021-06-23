# Jenkins Demo

```
virtualenv --python=python3 env/
source env/bin/activate
```

## Install Jenkins

```
helm repo add jenkinsci https://charts.jenkins.io
helm repo update
helm search repo jenkinsci

cat << EOH > values.yaml
controller:
  serviceType: LoadBalancer
  adminUser: "breqwatr"
  installPlugins:
    - kubernetes:1.29.4
    - workflow-aggregator:2.6
    - git:4.7.1
    - configuration-as-code:1.51
    - blueocean:1.24.7
    - kubernetes-cd:1.0.0
    - docker-workflow:1.26
    - docker-plugin:1.2.2
    - github:1.33.1
EOH

kubectl create ns jenkins
helm install jenkinsci jenkinsci/jenkins --values values.yaml --namespace jenkins
```
