#!/bin/bash

set -e

echo "[INFO] Creating Docker network..."
docker network create devops-network 2>/dev/null || echo "[INFO] Network already exists"

echo "[INFO] Starting database..."
docker-compose -f docker-compose-db.yml up -d --build

echo "[INFO] Waiting for database initialization (15 seconds)..."
sleep 15

echo "[INFO] Starting web server..."
docker-compose -f docker-compose-web.yml up -d --build

echo "[INFO] Waiting for services to start (10 seconds)..."
sleep 10

echo "[SUCCESS] Deployment complete!"
echo ""
echo "Access the application:"
echo "  Web:  http://localhost"
echo "  API:  http://localhost:8000"
echo "  Docs: http://localhost:8000/docs"
echo "  SSH:  ssh devops@localhost -p 2222 (password: devops123)"