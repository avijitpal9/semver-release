pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                sh "python3 -m build"
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
