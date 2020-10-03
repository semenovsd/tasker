# How to deploy:

1. Clone git project:

$ git clone git@github.com:semenovsd/tasker.git

2. Create .env file by the example.env in base tasker folder

3. Run bash script for install and settings Docker:

$ sudo bash entrypoint.sh

4. Build up docker containers:
$ docker-compose up --build
$ docker ps
$ docker exec -it <tasker_web container ID> python manage.py makemigrations --noinput
$ docker exec -it <tasker_web container ID> python manage.py migrate --noinput

Done!

# How to use:

1. Register new user

curl -X POST https://127.0.0.1/api/v1/auth/users/ --data 'username=djoser&password=alpine12'

Method POST /api/v1/auth/users/
data = {
    'username': 'djoser',
    'password': 'alpine12',
}

response: {"email": "", "username": "djoser", "id":1}

2. Get Token

curl -X POST https://127.0.0.1/api/v1/auth/token/login/ --data 'username=djoser&password=alpine12'

Method POST /api/v1/auth/token/login/
data = {
    'username': 'djoser',
    'password': 'alpine12',
}

response: {"auth_token": "b704c9fc3655635646356ac2950269f352ea1139"}

3. Check Authorization

curl -X POST https://127.0.0.1/api/v1/auth/users/ -H 'Authorization: Token <YOUR_TOKEN>'

Method GET /api/v1/auth/users/me/
Header: Authorization: Token <YOUR_TOKEN>

response: {"email": "", "username": "djoser", "id": 1}

4. Add task

POST tasks/add/
data = {
    'title': 'Сделать тестовое задание',
    'descriptions': 'Сделать тестовое задание согласно ТЗ',
    'status': 'Completed',
    'end_date': '2020-10-02',
}

5. View task

GET /tasks/pk
pk - int: task ID

6. Edit task

PUT /tasks/pk/
data = {
    'title': 'Сделать тестовое задание',
    'descriptions': 'Сделать тестовое задание согласно ТЗ',
    'status': 'Completed',
    'end_date': '2020-10-02',
}

7. Del task

DEL /tasks/pk/
pk - int: task ID

8. View all tasks with/without filters

GET /tasks/all/
