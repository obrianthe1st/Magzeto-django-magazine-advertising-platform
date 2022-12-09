# Docker

1. docker-compose

2. Clean up and rebuild docker volumes-

all you have to do is docker-compose down --volumes

next

docker-compose up -d --build --force-recreate

# Celery

http://localhost:5555/ (address to to view celery tasks)

docker-compose run celery sh -c "celery -A core.tasks worker --loglevel=INFO"

# Django

1. Create docker apps
   docker-compose run app sh -c "cd apps && django-admin startapp app1"

   INSTALLED_APPS = (
   'apps.app1',
   'apps.app2',)

   urlpatterns = patterns('',
   (r'^app1/',include('apps.app1')),  
    (r'^app2/',include('apps.app2')),)

   change configuration in apps.py file,
   class MyappConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   label='app1'
   name = 'apps.app1'

# Postgres

## logging into postgres

If you are logged into the same computer that Postgres is running on you can use the following psql login command, specifying the database (mydb) and username (myuser):

psql -d main_app -U postgres

If you need to log into a Postgres database on a server named myhost, you can use this Postgres login command:

psql -h db -d main_app -U postgres

- To view all tables of the db once logged in
  \d
