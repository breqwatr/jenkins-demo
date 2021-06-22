podTemplate(yaml: '''
    apiVersion: v1
    kind: Pod
    spec:
      containers:
      - name: test
        image: ubuntu:focal
        command:
        - sleep
        args:
        - 99d
      - name: jnlp
        image: 'jenkins/inbound-agent:4.7-1'
        args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
''') {
  node(POD_LABEL) {
    stage('Hello') {
      container('test') {
        sh 'echo HELLO WORLD - FROM KUBERNETES'
      }
    }
  }
}
