# How to deploy:

1. Clone git project:

$ git clone git@github.com:semenovsd/tasker.git

2. Create ssl cert:

$ cd /tasker/
$ mkdir .ssl
$ openssl req -newkey rsa:2048 -sha256 -nodes -keyout .ssl/url_private.key -x509 -days 365 -out .ssl/url_cert.pem

3. Create .env file by the example.env in base tasker folder

4. Run bash script for install and settings Docker:

$ sudo bash entrypoint.sh

5. Build up docker containers:
$ docker-compose up --build

Done!

# How to use:

1. Register new user
curl -X POST http://127.0.0.1:8000/api/v1/auth/users/ --data 'username=djoser&password=alpine12'
Method POST /api/v1/auth/users/
data params:
username - djoser
password - alpine12
response - {"email": "", "username": "djoser", "id":1}

2. Get Token
Method POST /api/v1/auth/token/login/
data params:
username - 
password - 
response - token

3. Check Authorization
curl -X POST http://127.0.0.1:8000/api/v1/auth/users/ -H 'Authorization: Token <YOUR_TOKEN>>'
Method GET /api/v1/auth/users/me/

4. Add task
POST tasks/add/

5. View task
GET /tasks/pk/

6. Edit task
PUT /tasks/pk/

7. Del task
DEL /tasks/pk/

8. View all tasks with/without filters
GET /tasks/all/
