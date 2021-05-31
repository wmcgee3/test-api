pipeline {

    agent {

        label 'master'

    }

    stages {

        stage('Create virtual environment.') {

            steps {

                sh 'python3 -m venv env'

            }

        }

        stage('Install dependencies.') {

            steps {

                sh 'env/bin/python -m pip install -r requirements.txt'

            }

        }

        stage('Run Pylint checks.') {

            steps {

                sh 'env/bin/python -m pylint test_api'

            }

        }

    }

}
