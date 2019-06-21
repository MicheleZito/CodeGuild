
# CodeGuild

CodeGuild is a web application that allows Computer Science students of the Università degli Studi di Napoli Parthenope,
to access a platform that lends them search for help in their Computer Science examsus. They can publish questions in the exams
sections and also reply to them. The web application uses the ESSE3 API (the same they use to access the services provided by the University).


# Installation
Tested on Ubuntu 16.04

Make sure you already have Python3 and pip installed.

### Clone the repository and create the virtual enviroment for Python 3
```sh
$ git clone https://github.com/MicheleZito/CodeGuild.git
$ cd CodeGuild
$ python3 -m venv venv
```
### Activate the environment 
```sh
$ . venv/bin/activate
```
### Install the required dependecy
```sh
$ pip install -r requirements.txt
```

### Set Environment variable for Flask and initialize database
```sh
$ cd codeguild
$ export FLASK_APP=codeguild
$ flask init-db
```

### Run the server
```sh
$ flask run
```

Now the app is running on localhost using the port 5000.
If you want to run the application with an IP used by a machine in your network, on another port, you can use the following:
```sh
$ flask run -h 192.168.0.7 -p 5000
```
In this example, after starting the server, the app will be found at http://192.168.0.7:5000