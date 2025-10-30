# DevOps Lab: Docker Environment Setup

Project demonstrating DevOps infrastructure with Docker, NGINX, PostgreSQL, and FastAPI.

## Quick Start

### Automatic deployment:
```bash
./deploy.sh
```

### Manual deployment:
```bash
docker network create devops-network
docker-compose -f docker-compose-db.yml up -d --build
docker-compose -f docker-compose-web.yml up -d --build
```

## Access Services

- Web: http://localhost
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- SSH: ssh devops@localhost -p 2222 (password: devops123)
- PostgreSQL: localhost:5432 (user: devops, password: devops123)

## Useful Commands

```bash
# View logs
docker logs web-server
docker logs db-server

# Enter containers
docker exec -it web-server bash
docker exec -it db-server bash

# Connect to PostgreSQL
docker exec -it db-server psql -U devops -d devops_lab

# Check connectivity
docker exec web-server ping db-server -c 4

# Stop services
docker-compose -f docker-compose-web.yml down
docker-compose -f docker-compose-db.yml down
```

## API Endpoints

- `GET /` - Main page with user list
- `GET /api/users` - All users (JSON)
- `GET /api/users/{id}` - User by ID
- `GET /health` - Health check