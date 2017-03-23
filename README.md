# Xenon (formerly Neon) Web API for WS Companion

## Features:
* Creates an API for use by the [WS Companion app](https://github.com/MaldorLevr/xenon) which it uses to give updated information for students of Windsor Secondary
* Automagically scrapes calendar data from Windsor Secondary's website in order to automate the adding of information to the app
* Uses [Ionic's Push API](https://docs.ionic.io/services/push/) to send notifications to Windsor Secondary students about important events
* Stores teacher contact information for easy access with the [WS Companion app](https://github.com/MaldorLevr/xenon)

--------------------------------------------------------------------------------

## Technologies used
* [Python 3.x](https://www.python.org/)
* [Django](https://www.djangoproject.com/) ([and accompanying libraries](https://github.com/MaldorLevr/neon-webapp/blob/master/requirements.txt))
* [Git](https://git-scm.com/)
* [Nginx](https://www.nginx.com/resources/wiki/)
* Web APIs ([Ionic](http://ionic.io/))
* MySQL ([MariaDB](https://mariadb.org/))
* HTML
* [Ubuntu Server](http://www.ubuntu.com/download/server)
* [Bash](https://www.gnu.org/software/bash/) shell and bash tools
* Ubuntu tools ([Supervisor](http://supervisord.org/), [Gunicorn](http://gunicorn.org/)), and more)
* [Huey](https://huey.readthedocs.io/en/latest/) paired with [Redis](http://redis.io/)

--------------------------------------------------------------------------------

## Development Setup Guide
Commands are for Windows but are easily adaptable to Linux.

1. [Download](https://www.python.org/downloads/) and install the latest version of Python 3
2. [Download](https://git-scm.com/downloads) and install the latest version of git
3. Open Git Bash and clone this GitHub repo by running the command `git clone https://github.com/MaldorLevr/neon-webapp.git`
4. Install virtualenv by running the command `pip install virtualenv` (may need to be running Git bash as an administrator)
5. Create a virtual environment by running the command `virtualenv env` and activate it by running the command `.\testenv\Scripts\activate`.
6. Switch to the project directory with `cd neon-webapp` and run `pip install -r requirements.txt` to install the required packages.
7. Run the server with `python manage.py runserver` and view the server by opening your browser and going to the address `localhost:8000`. If you see this image you've successfully started up the web app! ![](http://i.imgur.com/gDY05yw.png)
8. Stop the server by going into Git bash again and pressing Ctrl + C
9. Create a superuser account for yourself by running the command `python manage.py createsuperuser`
10. Run the server again and this time navigate to `localhost:8000/admin` in your browser and login. From here you should be able to create some test data.