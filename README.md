# Magzeto-django-magazine-advertising-platform

This is just a quick mockup of a django project I decided to create of a newspaper frontend and advertising backend over the span of a few hours on couple days a week.

It's a prototype to see how I would implement various functionalities, most of the functionalities are a bit rudimentary and shouldn't be used in the wild 
at all. You are free to have a look at it though.


# Newspaper section
-----------------------------------------------


https://user-images.githubusercontent.com/88407652/217941459-86f283e9-e44a-4512-9132-b6c9d8bbc4d4.mp4



# advertising section
----------------------------------------------


https://user-images.githubusercontent.com/88407652/217938532-dcdc9f46-3566-46b7-8da5-4df8fee77633.mp4


I use docker to manage the different applications such as postgresql, redis, celery.

Command to spin up services:

```
docker-compose up
```

command to run application:

```
docker-compose run app sh -c "python manage.py runserver"
```
