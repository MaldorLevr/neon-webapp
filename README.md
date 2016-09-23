# Xenon (formerly Neon) Web for WS Companion

## Features:
* Creates an API for use by the [WS Companion app](https://github.com/MaldorLevr/xenon) which it uses to give updated information for students of Windsor Secondary
* Automagically scrapes calendar data from Windsor Secondary's website in order to automate the adding of information to the app
* Uses [Ionic's Push API](https://docs.ionic.io/services/push/) to send notifications to Windsor Secondary students about important events
* Stores teacher contact information for easy access with the [WS Companion app](https://github.com/MaldorLevr/xenon)

## Technologies used
* [Python 3.x](https://www.python.org/)
* [Django](https://www.djangoproject.com/) ([and accompanying libraries](https://github.com/MaldorLevr/neon-webapp/blob/master/requirements.txt))
* [Huey](https://huey.readthedocs.io/en/latest/) paired with [Redis](http://redis.io/)
* Web APIs ([Ionic](http://ionic.io/))
* MySQL ([MariaDB](https://mariadb.org/))
* HTML
* [Ubuntu Server](http://www.ubuntu.com/download/server)
* [Bash](https://www.gnu.org/software/bash/) shell
* Ubuntu tools ([Supervisor](http://supervisord.org/), [Gunicorn](http://gunicorn.org/)), and more)
