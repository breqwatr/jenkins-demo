# To install Jenkins
helm repo add jenkinsci https://charts.jenkins.io
helm repo update
helm install jenkinsci jenkinsci/jenkins --values values.yaml --namespace jenkins
