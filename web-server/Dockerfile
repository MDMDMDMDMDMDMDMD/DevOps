FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    nginx \
    python3 \
    python3-pip \
    git \
    openssh-server \
    sudo \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash devops && \
    echo "devops:devops123" | chpasswd && \
    usermod -aG sudo devops

RUN mkdir -p /opt/app /opt/db && \
    chown -R devops:devops /opt/app /opt/db

RUN mkdir /var/run/sshd && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

RUN pip3 install fastapi uvicorn psycopg2-binary python-multipart jinja2

RUN git config --global user.name "DevOps Student" && \
    git config --global user.email "devops@example.com"

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

WORKDIR /opt/app

CMD ["/startup.sh"]