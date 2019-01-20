FROM python:3.6

# apt
RUN apt-get update && \ 
    apt-get install -y vim

# pip
RUN pip install redis && \
    pip install celery[redis] && \
    pip install awscli && \
    pip install boto3

# User
WORKDIR /home/celery/
ENV PYTHONPATH /home/celery/

# AWS
ENV AWS_SHARED_CREDENTIALS_FILE /home/celery/proj/.aws/credentials
ENV AWS_DEFAULT_REGION ap-northeast-1

CMD celery -A proj worker -l info
