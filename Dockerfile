FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \ 
<<<<<<< HEAD
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
     && apk add libffi-dev 
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps



RUN mkdir /src
COPY ./src /src
WORKDIR /src

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web/
USER user
=======
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
COPY ./app /app
WORKDIR /app
>>>>>>> 69355aff134f4efa893df922943e88abcff70792
