pipeline {
    agent {
        label 'master'
    }

    stages {

        stage('Create virtual environment') {

            when {
                expression {
                    (env.BRANCH_NAME.startsWith('PR-') && env.CHANGE_TARGET == 'dev') || (
                        env.BRANCH_NAME == 'prod'
                    )
                }
            }

            steps {
                sh 'python3 -m venv env'
            }

        }

        stage('Install dependencies') {

            when {
                expression {
                    (env.BRANCH_NAME.startsWith('PR-') && env.CHANGE_TARGET == 'dev') || env.BRANCH_NAME == 'prod'
                }
            }

            steps {
                sh 'env/bin/python -m pip install -r requirements.txt'
            }

        }

        // PR only
        stage('Linting') {

            when {
                expression {
                    (env.BRANCH_NAME.startsWith('PR-') && env.CHANGE_TARGET == 'dev')
                }
            }

            steps {
                sh 'env/bin/python -m pylint test_api'
            }

        }

        // prod only
        stage('Create database.') {

            when {
                expression {
                    env.BRANCH_NAME == 'prod'
                }
            }

            steps {
                sh 'rm test_api/test.db'
                sh 'env/bin/python init_db.py'
            }

        }

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
