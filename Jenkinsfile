pipeline {
    agent any

    environment {
        PYTHON_DIR = 'C:\\Users\\Pc\\AppData\\Local\\Programs\\Python\\Python311'
        PATH = "${PYTHON_DIR};${PYTHON_DIR}\\Scripts;${env.PATH}"
    }

    stages {
        stage('Vérification Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip --version'
            }
        }
        stage('Installation des dépendances') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Analyse qualite code -Pylint'){
            steps {
                bat 'python -m pylint calculator.py || exit /b 0'

            }
        }
        stage('Tests unitaires') {
            steps {
                bat 'python -m pytest'
            }
        }
        stage(' Creation de l artefact'){
            steps {
                bat '''
                if exist Release rmdir /S/Q Release
                mkdir Release

                copy calculator.py Release
                copy test_calculator.py Release
                copy requirements.txt Release
                '''
            }
        }
    }

    post {
        always  { echo 'Pipeline terminé' }
        success { echo 'BUILD SUCCESS' }
        failure { echo 'BUILD FAILED' }
    }
}