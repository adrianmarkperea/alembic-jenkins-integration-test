pipeline {
  agent {
    docker { image 'python:3' }
  }
  stages {
    stage('build') {
      steps {
        script {
          echo 'building alembic-runner'
          sh 'chmod +x build.sh'
        }
      }
    }
    stage('execute') {
      withEnv(["HOME=${env.WORKSPACE}"]) {
          echo 'executing alembic-runner'
          sh 'python3 -m pip install alembic==1.7.7'
          sh 'chmod +x deploy.sh'
          sh './deploy.sh'
          sh 'chmod +x execute.sh'
          sh './execute.sh'
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
