pipeline {

    agent {
        kubernetes {
        label 'jenkins-slave'
        defaultContainer 'jnlp'
        yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: some-label-value
spec:
  volumes:
  - name: traindata
    persistentVolumeClaim:
      claimName: traindata
  containers:
  - name: python
    image: python:3.7.2-slim
    volumeMounts:
    - name: traindata
      mountPath: /data
    env:
    - name: MONGODB_URL
      valueFrom:
        secretKeyRef:
          key: mongodb
          name: db-user-pass
    - name: MONGODB_USER
      valueFrom:
        secretKeyRef:
          key: user
          name: db-user-pass
    - name: MONGODB_PASSWORD
      valueFrom:
        secretKeyRef:
          key: password
          name: db-user-pass
    - name: AWS_ACCESS_KEY_ID
      valueFrom:
        secretKeyRef:
          key: AWS_ACCESS_KEY_ID
          name: s3reader
    - name: AWS_SECRET_ACCESS_KEY
      valueFrom:
        secretKeyRef:
          key: AWS_SECRET_ACCESS_KEY
          name: s3reader
    command:
    - cat
    tty: true
"""
        }
    }

  
    stages{
        stage('Download requirements'){
            steps{
                container('python'){
                    sh 'apt update'
                    sh 'apt install libgomp1'
                    sh 'pip install -r requirements.txt'
                    sh 'pip install -U pytest'
                }
            }
        }
        stage('pytest') {
            steps{
                container('python'){
                    sh 'py.test model.py --junitxml=pytest_report.xml'
                }
            }
        }
        stage('Run model') {
            steps{
                container('python'){
                    sh 'python model.py --mongodb ${MONGODB_URL} --user ${MONGODB_USER} --password ${MONGODB_PASSWORD} --datapath /data'
                }
            }
        }
        
        stage('publish docker image'){}
    }
    
}
