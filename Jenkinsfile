pipeline {
    agent {
        label 'master'
    }

    stages {

        stage('Create virtual environment') {

            steps {
                sh 'python3 -m venv env'
            }

        }

        stage('Install dependencies') {

            steps {
                sh 'env/bin/python -m pip install -r requirements.txt'
            }

        }

        // PR only
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

        // prod only
        stage('Restart web server.') {

            when {
                expression {
                    env.BRANCH_NAME == 'prod'
                }
            }

            steps {
                sh 'sudo systemctl restart test-api'
                sh 'sudo systemctl restart nginx'
            }

        }
    }
}
