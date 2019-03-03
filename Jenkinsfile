pipeline {

    agent {
        kubernetes {
        label 'jenkinspod'
        defaultContainer 'jnlp'
        yamlFile 'k8spod.yaml'
        }
    }

  
    stages{
        stage('Download requirements'){
            steps{
                sh 'apt update'
                sh 'apt install libgomp1'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run model') {
            steps{
                sh 'python model.py --mongodb ${MONGODB_URL} --user ${MONGODB_USER} --password ${MONGODB_PASSWORD} --datapath /data'
            }
        }
    }
    
}