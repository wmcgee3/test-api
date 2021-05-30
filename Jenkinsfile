pipeline {
    agent none

    stages {
        stage('Create virtual environment') {
            when {
                expression {
                    branch == 'PR-*'
                }
            }
            steps {
                sh 'python3 -m venv env'
            }
        }
        stage('Install dependencies') {
            when {
                expression {
                    branch == 'PR-*'
                }
            }
            steps {
                sh 'env/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Linting') {
            when {
                expression {
                    branch == 'PR-*'
                }
            }
            steps {
                sh 'env/bin/python -m pylint test_api'
            }
        }
    }
}