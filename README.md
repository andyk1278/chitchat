# ChitChat
A real-time chat application built on Django/Django Rest Framework, Vue, uWSGI Websockets, and RabbitMQ.

# Usage
### Vue (frontend)
Change directory into "chitchat-frontend" directory:

cd chitchat-frontend

Install the dependencies via npm:

npm install

Run the webpack dev server (defaults to localhost:8080)

npm run dev


### Django
To successfully run the Django server..

Change directories into the root project folder:

cd andyk1278/chitchat

Install the python package requirements via pip:

pip install -r requirements.txt

Run django's development server (defaults to localhost:8000)

python manage.py runserver


### RabbitMQ
ChitChat uses RabbitMQ to connect the django application and the uWSGI Websocket server. Depending on your operating system, the installation steps vary.
Refer to the docs on how to correctly install it on your operating system.


### Websocket server
ChitChat uses uWSGI as the websocket server and if you have already install the python package requirements listed in 'requirements.txt', it has already been installed!

You can start the websocket server with the following command:

uswgi --http :8081 --gevent 100 --module websocket --gevent-monkey-path --master
