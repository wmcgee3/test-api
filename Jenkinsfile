pipeline {
    agent {
        label 'master'
    }

    stages {
        stage('Create virtual environment') {
            when {
                expression {
                    env.BRANCH_NAME.startsWith('PR-')
                }
            }
            steps {
                sh 'python3 -m venv env'
            }
        }
        stage('Install dependencies') {
            when {
                expression {
                    env.BRANCH_NAME.startsWith('PR-')
                }
            }
            steps {
                sh 'env/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Linting') {
            when {
                expression {
                    env.BRANCH_NAME.startsWith('PR-')
                }
            }
            steps {
                sh 'env/bin/python -m pylint test_api'
            }
        }
    }
}