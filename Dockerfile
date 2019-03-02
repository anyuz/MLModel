FROM python:3.7.2-slim

RUN apt update
RUN apt install libgomp1

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt


CMD python model.py \
        --mongodb ${MONGODB_URL} \
        --user ${MONGODB_USER} \
        --password ${MONGODB_PASSWORD} \
        --datapath /data