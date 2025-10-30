FROM postgres:15

RUN useradd -m -s /bin/bash devops && \
    echo "devops:devops123" | chpasswd

RUN mkdir -p /opt/db && \
    chown -R postgres:postgres /opt/db

RUN apt-get update && apt-get install -y \
    vim \
    curl \
    && rm -rf /var/lib/apt/lists/*