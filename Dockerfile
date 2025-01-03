FROM jenkins/jenkins:lts

USER root

# Install Python and required tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv python3-flask && \
    apt-get clean

USER jenkins
