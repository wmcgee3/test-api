node {

    if (env.BRANCH_NAME.startsWith('PR-')) {

        stage('Create virtual environment.') {
            sh 'python3 -m venv env'
        }

        stage('Install required packages.') {
            sh 'env/bin/python -m pip install -r requirements.txt'
        }

        stage('Run linting checks.') {
            sh 'env/bin/python -m pylint test_api'
        }

    }

}
