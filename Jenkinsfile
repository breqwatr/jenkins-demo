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
    stage('BUILD') {
      git 'https://github.com/breqwatr/jenkins-demo.git'
      container('docker') {
        stage('build: lib') {
          sh '''
             cd lib
             docker build -t breqwatr/applib:latest .
             docker tag breqwatr/applib:latest breqwatr/applib:jenkins-1
             '''
        }
        stage('test: lib') {
          sh 'docker run --rm breqwatr/applib pytest /app/lib/test/'
        }
        stage('build: api') {
          sh '''
             cd api
             docker build -t breqwatr/appapi:latest .
             docker tag breqwatr/appapi:latest breqwatr/appapi:jenkins-1
             '''
        }
        stage('test: api') {
          sh 'docker run --rm breqwatr/appapi pytest /app/api/test/'
        }
      }
    }
    stage('DEPLOY') {
      kubernetesDeploy(configs: "manifest.yaml")
    }
    stage('FINISH') {
      container('docker') {
        stage('rejoice') {
          sh "docker run breqwatr/cowsay /usr/games/cowsay 'Jenkins with Kubernetes on Breqwatr rocks!'"
        }
      }
    }
  }
}
