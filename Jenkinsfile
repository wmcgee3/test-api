pipeline {
    agent master

    stages {
        when {
            expression {
                branch == 'PR-*'
            }
        }
        stage('Create virtual environment') {
            steps {
                sh python3 -m venv env
            }
        }
        stage('Install dependencies') {
            steps {
                sh env/bin/python -m pip install -r requirements.txt
            }
        }
        stage('Linting') {
            steps {
                sh env/bin/python -m pylint test_api
            }
        }
    }
}