pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('AI Pre-Deployment Analysis') {
            steps {
                sh '''
                    cd ai_engine

                    python3 -m venv venv

                    venv/bin/python -m pip install -r requirements.txt

                    venv/bin/python decision_engine.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ai-self-healing-app:1.0 -f docker/Dockerfile .
                '''
            }
        }

        stage('Deployment') {
            steps {
                sh '''
                    docker save -o /tmp/ai-self-healing-app-1.0.tar ai-self-healing-app:1.0

                    scp -i /var/lib/jenkins/.ssh/id_ed25519 \
                        -o IdentitiesOnly=yes \
                        /tmp/ai-self-healing-app-1.0.tar \
                        megaproject@10.216.251.35:/tmp/

                    ssh -i /var/lib/jenkins/.ssh/id_ed25519 \
                        -o IdentitiesOnly=yes \
                        megaproject@10.216.251.35 \
                        'sudo -n /usr/bin/ctr -n k8s.io images import /tmp/ai-self-healing-app-1.0.tar && \
                         kubectl apply -f ~/k8s/deployment.yaml && \
                         kubectl apply -f ~/k8s/service.yaml && \
                         kubectl rollout status deployment/ai-self-healing-app -n ai-self-healing'
                '''
            }
        }
    }
}
