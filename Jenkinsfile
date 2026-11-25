pipeline {
    agent any

    environment {
        PYTHON_DIR = 'C:\\Users\\Pc\\AppData\\Local\\Programs\\Python\\Python311'
        PATH = "${PYTHON_DIR};${PYTHON_DIR}\\Scripts;${env.PATH}"
    }

    stages {
        stage('Nettoyage') {
            steps {
                bat '''
                if exist Release rmdir /S /Q Release
                if exist Release.zip del /Q Release.zip
                '''
            }
        }

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

        stage('Analyse qualite code - Pylint') {
            steps {
                bat 'python -m pylint calculator.py || exit /b 0'
            }
        }

        stage('Tests unitaires') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Creation de l artefact') {
            steps {
                bat '''
                if exist Release rmdir /S /Q Release
                if exist Release.zip del /Q Release.zip
                mkdir Release
                copy calculator.py Release
                copy test_calculator.py Release
                copy requirements.txt Release
                powershell -Command "Compress-Archive -Path Release\\* -DestinationPath Release.zip -Force"
                '''
                archiveArtifacts artifacts: 'Release.zip', fingerprint: true
            }
        }

        stage('Publication de l artefact') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'nexus-credentials',
                                                  usernameVariable: 'admin',
                                                  passwordVariable: 'fd1c26ae-6590-46ec-942e-119fb06734d5')]) {
                    bat '''
                    curl -v ^
                    -u %NEXUS_USER%:%NEXUS_PASS% ^
                    --upload-file Release.zip ^
                    http://localhost:8081/repository/python-release/Release.zip
                    '''
                }
            }
        }
    }

    post {
        always  { echo 'Pipeline terminé' }
        success { echo 'BUILD SUCCESS' }
        failure { echo 'BUILD FAILED' }
    }
}