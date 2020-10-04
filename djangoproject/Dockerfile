# base image for django project
FROM python:3.8.6

ARG DJANGO_BASE_DIR
ARG STATIC_FILES
ARG MEDIA_FILES

# Set work dir
WORKDIR /DJANGO_BASE_DIR

## create the app user
#RUN addgroup -S django && adduser -S django -G django

# Create static and media folders
RUN mkdir STATIC_FILES
RUN mkdir MEDIA_FILES

# The enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .

## chown all the files to the app user
#RUN chown -R django:django DJANGO_BASE_DIR

## Change to the app user
#USER django

#bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
# Prepare Django to start
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "collectstatic"]
