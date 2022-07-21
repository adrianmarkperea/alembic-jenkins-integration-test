pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        script {
          echo 'building alembic-runner'
          sh 'chmod +x build.sh'
          sh './build.sh'
        }
      }
    }
    stage('execute') {
      steps {
        script {
          echo 'executing alembic-runner'
          sh 'apt-get install -y libpq-dev'
          sh 'pip install -r requirements.txt'
          sh 'chmod +x deploy.sh'
          sh './deploy.sh'
          sh 'chmod +x execute.sh'
          sh './execute.sh'
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
