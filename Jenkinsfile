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
    stage('INIT') {
      git 'https://github.com/breqwatr/jenkins-demo.git'
      container('docker') {
        stage('Build the library docker image') {
          sh '''
             cd lib
             docker build -t breqwatr/applib:latest .
             docker tag breqwatr/applib:latest breqwatr/applib:jenkins-1
             '''
        }
        stage('Test: lib') {
          sh 'docker run --rm breqwatr/applib pytest /app/lib/test/'
        }
        stage('Build the api docker image') {
          sh '''
             cd api
             docker build -t breqwatr/appapi:latest .
             docker tag breqwatr/appapi:latest breqwatr/appapi:jenkins-1
             '''
        }
        stage('Test: api') {
          sh 'docker run --rm breqwatr/appapi pytest /app/api/test/'
        }
        stage('Rejoice') {
          sh "docker run breqwatr/cowsay /usr/games/cowsay 'Jenkins with Kubernetes on Breqwatr rocks!'"
        }
      }
    }
  }
}
