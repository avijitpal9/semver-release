pipeline{
    agent {
        docker { image 'python:3.7-alpine' }
    }
    stages{
        stage("Build"){
            steps{
                sh "python3 --version "
            }
        }
    }
    post{
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}
