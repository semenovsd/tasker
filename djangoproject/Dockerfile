# base image for django project
FROM python:3.8.6

ARG APP_BASE_DIR

WORKDIR /APP_BASE_DIR

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations && python manage.py migrate
