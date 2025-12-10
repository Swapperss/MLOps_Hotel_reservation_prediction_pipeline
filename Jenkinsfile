pipeline{
    agent any

        environment{
            VENV_DIR = 'venv'
            GCP_PROJECT = "mlops-479111"
            GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Swapperss/MLOps_Hotel_reservation_prediction_pipeline.git']])
                }
            }
        }

        stage('Setting up Python Virtual Environment and Installing Dependencies'){
            steps{
                script{
                    echo 'Setting up Python Virtual Environment and Installing Dependencies'
                    sh '''
                        apt-get update && apt-get install -y python3.11 python3.11-venv python3.11-distutils
                        python3.11 -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        python3.11 -m pip install --upgrade pip
                        python3.11 -m pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Building and pushing Docker image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script{
                        echo 'Building and pushing Docker image to GCR.............'
                        sh '''
                            . ${VENV_DIR}/bin/activate
                            export PATH=${GCLOUD_PATH}:$PATH
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJECT}
                            gcloud auth configure-docker --quiet
                            IMAGE_NAME="gcr.io/${GCP_PROJECT}/hotel-reservation-prediction:latest"
                            docker build -t $IMAGE_NAME .
                            docker push $IMAGE_NAME
                        '''
                    }
                }
            }
        }
    }
}