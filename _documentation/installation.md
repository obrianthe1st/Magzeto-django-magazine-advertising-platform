# Docker

# Github

# Django

## Setting up apps folder

### docker commands

- command to create application in apps folder
  docker-compose run app sh -c "cd apps && django-admin startapp app1"

INSTALLED_APPS = (
'apps.app1',
'apps.app2',)

urlpatterns = patterns('',
(r'^app1/',include('apps.app1.urls')),  
 (r'^app2/',include('apps.app2.urls')),)

change configuration in apps.py file,
class MyappConfig(AppConfig):
default_auto_field = 'django.db.models.BigAutoField'
label='app1'
name = 'apps.app1'

I use an apps folder within project directory to store all my applications. This makes it easier to
test features.

## Setting up sphinx

Youtube link for clarification:

https://www.youtube.com/watch?v=BWIrhgCAae0

-command to setup sphinx meta data for our sphinx project
sphinx-quickstart

-command which basically generates the documentation for you
sphinx-apidoc -o docs .

-command to build file into html
.\make.bat html
