pipeline {
  environment {
    JENKINS_SECRET = 'Jenkins with Kubernetes on Breqwatr rocks!'
  }
  agent {
    kubernetes {
      yaml '''
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
            env:
              - name: JENKINS_SECRET
                value: env.JENKINS_SECRET
              - name: DOCKER_USERNAME
                valueFrom:
                  secretKeyRef:
                    name: dockerhub
                    key: username
              - name: DOCKER_PASSWORD
                valueFrom:
                  secretKeyRef:
                    name: dockerhub
                    key: password
            volumeMounts:
            - mountPath: /var/run/docker.sock
              name: docker-socket
            command:
            - sleep
            args:
            - 99d
    '''
    }
  }
  stages {
    stage('BUILD') {
      steps {
        git 'https://github.com/breqwatr/jenkins-demo.git'
        sh '''
           cd lib
           docker build -t breqwatrdemo/applib:latest .
           cd ../api
           docker build -t breqwatrdemo/appapi:latest .
           '''
      }
    }
    stage('TEST') {
      steps {
        sh 'docker run --rm breqwatrdemo/applib pytest /app/lib/test/'
        sh 'docker run --rm breqwatrdemo/appapi pytest /app/api/test/'
      }
    }
    stage('PUSH') {
      steps {
        sh 'docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD'
        sh 'docker push breqwatrdemo/applib'
        sh 'docker push breqwatrdemo/appapi'
      }
    }
    stage('DEPLOY') {
      steps {
        kubernetesDeploy(configs: "manifest.yml", enableConfigSubstitution: true, kubeconfigId: "kubeconfig")
      }
    }
    stage('REJOICE') {
      steps {
        sh 'docker run breqwatr/cowsay /usr/games/cowsay "$JENKINS_SECRET"'
      }
    }
  }
}
