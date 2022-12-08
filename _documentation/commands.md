# Docker

1. docker-compose

2. Clean up and rebuild docker volumes-

all you have to do is docker-compose down --volumes

next

docker-compose up -d --build --force-recreate

3.

# Celery

http://localhost:5555/ (address to to view celery tasks)

docker-compose run celery sh -c "celery -A core.tasks worker --loglevel=INFO"

# Django

# Postgres
