pipeline {
    agent { label 'one' }

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository'
                git branch: 'main', url: 'https://github.com/sharad46792/python-web-app.git'
            }
        }

        stage('Build Image') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t python-web-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Running container'
                sh '''
                  docker rm -f python-web-app || true
                  docker run -d -p 2000:2000 --name python-web-app python-web-app:latest
                '''
            }
        }
    }
}
