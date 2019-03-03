pipeline {

    agent {
        kubernetes {
        label 'jenkinspod'
        defaultContainer 'jnlp'
        yamlfile 'k8spod.yaml'
        }
    }

  
    stages{
        stage('Download requirements'){
            steps{
                apt update
                apt install libgomp1
                pip install -r requirements.txt
            }
        }
        stage('Run model') {
            steps{
                python model.py --mongodb ${MONGODB_URL} --user ${MONGODB_USER} --password ${MONGODB_PASSWORD} --datapath /data
            }
        }
    }
    
}