pipeline {
  agent {
    docker { image 'python:3' }
  }
  stages {
    stage('execute') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          echo 'executing alembic-runner'
          sh 'python3 -m pip install -r requirements.txt'
          sh 'chmod +x execute.sh'
          source './execute.sh'
          sh 'chmod +x deploy.sh'
          sh './deploy.sh'
        }
      }
    }
    stage('clean') {
      steps {
        script {
          echo 'cleaning alembic-runner'
          sh 'chmod +x clean.sh'
          sh './clean.sh'
        }
      }
    }
  }
}
