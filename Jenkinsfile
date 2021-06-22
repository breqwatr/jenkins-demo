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
        sh '''#!/bin/bash
             echo "hello world 1"
        '''
			}
		}
  }
}
