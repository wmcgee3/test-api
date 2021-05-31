pipeline {
    agent {
        label 'master'
    }

    stages {

        stage('Print branch name.') {

            steps {
                echo env.BRANCH_NAME
            }

        }

    }
}
