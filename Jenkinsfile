pipeline {
  environment {
    libDockerImage = 'breqwatr/appLib'
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/breqwatr/jenkins-demo', branch: 'master'])
      }
    }
    stage('Running a thing') {
			steps {
        sh 'apt-get update'
        sh 'apt-get install -y docker-ce'
        sh '''#!/bin/bash
             echo "hello world 1"
             echo "hello world 2"
             ls
             whoami
             pwd
             echo $libDockerImage
             cd lib
             ./build.sh
        '''
			}
		}
  }
}
