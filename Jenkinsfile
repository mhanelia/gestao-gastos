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
                sh 'python -m unittest discover tests' 
            }
            
               stage('Code Quality Check via SonarQube') {
	   stage('SonarQube analysis') {
    def scannerHome = tool 'SonarScanner 4.0';
    withSonarQubeEnv('My SonarQube Server') { // If you have configured more than one global server connection, you can specify its name
      sh "${scannerHome}/bin/sonar-scanner"
    }

	   }
            
        }
    }
}

