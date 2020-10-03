# base image for django project
FROM python:3.8.6-alpine

ARG DJANGO_BASE_DIR

## create the app user
#RUN addgroup -S app && adduser -S app -G app
#RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/staticfiles
#RUN mkdir $APP_HOME/mediafiles

# Set work dir
WORKDIR /DJANGO_BASE_DIR

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

## chown all the files to the app user
#RUN chown -R app:app $APP_HOME
## change to the app user
#USER app
