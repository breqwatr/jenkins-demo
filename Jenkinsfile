podTemplate(yaml: '''
    apiVersion: v1
    kind: Pod
    spec:
      volumes:
      - hostPath:
          path: /var/run/docker.sock
          type: ""
        name: docker-socket
      containers:
      - name: jnlp
        image: 'jenkins/inbound-agent:4.7-1'
        args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
      - name: docker
        image: docker
        volumeMounts:
        - mountPath: /var/run/docker.sock
          name: docker-socket
        command:
        - sleep
        args:
        - 99d
''') {
  node(POD_LABEL) {
    stage('Build the Docker image') {
      git 'https://github.com/breqwatr/jenkins-demo.git'
      container('docker') {
        stage('Build a docker image') {
          sh 'pwd'
          sh 'ls'
          sh 'find .'
        }
      }
    }
  }
}
