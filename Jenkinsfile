pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.12.0-alpine3.18' 
                }
            }
            steps {
                withSonarQubeEnv('sq') { // If you have configured more than one global server connection, you can specify its name
                sh "${scannerHome}/bin/sonar-scanner"
                }
	       }
        }
    }
}

