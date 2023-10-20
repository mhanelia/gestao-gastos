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
        }
    }
}

