# base image for django project
FROM python:3.8.6-alpine

ARG APP_BASE_DIR

WORKDIR /APP_BASE_DIR

COPY ../requirements.txt /APP_BASE_DIR

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY .. /APP_BASE_DIR

RUN python manage.py makemigrations && python manage.py migrate
