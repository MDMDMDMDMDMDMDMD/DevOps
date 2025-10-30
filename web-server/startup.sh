#!/bin/bash

service ssh start
service nginx start

cd /opt/app

if [ ! -d "/opt/app/.git" ]; then
    echo "Git repository not initialized yet"
fi

if [ -f "/opt/app/main.py" ]; then
    uvicorn main:app --host 0.0.0.0 --port 8000 &
fi

tail -f /dev/null