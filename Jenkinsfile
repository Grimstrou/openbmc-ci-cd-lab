// Jenkinsfile
pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = "1"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Замени URL на свой репозиторий!
                git branch: 'main', url: 'https://github.com/Grimstrou/openbmc-ci-cd-lab'
            }
        }

        stage('Start QEMU with OpenBMC') {
            steps {
                sh '''
                    echo "=== Starting QEMU with OpenBMC (simulation) ==="
                    echo "[QEMU] Booting OpenBMC image for Romulus platform..." > qemu.log
                    echo "[QEMU] Kernel loaded. BMC IP: 127.0.0.1, SSH port: 2200" >> qemu.log
                    echo "[QEMU] System ready in 5 seconds." >> qemu.log
                    sleep 5
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'qemu.log', fingerprint: true
                }
            }
        }

        stage('Run Auto Tests') {
            steps {
                sh 'python3 tests/auto_test.py'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'auto_test_report.xml', fingerprint: true
                    junit 'auto_test_report.xml'
                }
            }
        }

        stage('Run WebUI Tests') {
            steps {
                sh 'python3 tests/webui_test.py'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'webui_test_report.xml', fingerprint: true
                    junit 'webui_test_report.xml'
                }
            }
        }

        stage('Run Load Testing') {
            steps {
                sh 'python3 tests/load_test.py'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'load_test_report.txt', fingerprint: true
                }
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD pipeline completed successfully!'
        }
        failure {
            echo '❌ CI/CD pipeline failed!'
        }
    }
}