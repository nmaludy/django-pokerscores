[![Build Status](https://circleci.com/gh/nmaludy/django-pokerscores.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/nmaludy/django-pokerscores) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Poker Leaderboard App

## Data

League
 - name
 - List[User]
 - List[Player]
 - List[Season]
 
User
 - name
 - email
 - password
 - League
 
Player
 - name
 - email
 - Scores (tournaments played)
 
Season
 - name
 - League
 - start date (optional)
 - end date (optional)
 - List[Tournament]
 - active
 - visible
 
Tournament
 - name
 - start date (optional)
 - end date (optional)
 - League
 - Optional[Season]
 - List[Score]
 - ScoringSystem
 
Score
 - Player
 - points
 - Tournament
 
ScoringSystem
 - name
 - List[int] - points per place

TODO: History
 - Score history (something)

Leaderboard
 - select a season
 - select a tournament (optional)
 - show Players with their total Scores in the Season (and Tournament, optional)
 - sort players by rank or by name

## Steps

Setup environment

``` shell
virtualenv virtualenv
source ./virtualenv/bin/activate
pip install -r requirements.txt
```

**NOTE** All following steps assume you're in the `pokerscores/` directory and have the `virtualenv/` activated.

**YOU DON"T NEED TO DO THIS**. This is how i setup the project initially.

``` shell
django-admin startproject pokerscores
python manage.py startapp api
```

Initialize the database

``` shell
python manage.py migrate
```

Run the test server (dev only)

``` shell
DATABASE_PASSWORD=PokerScores123 python manage.py runserver
```

Test out the site by going to [http://localhost:8000/api](http://localhost:8000/api)


## Editing models

Edit or model code

Creating migrations
``` shell
python manage.py makemigrations api
```

Run the migrations, note the number will be created above and will be different that `0001`

``` shell
python manage.py sqlmigrate api 0001
```

## Starting Database container

Prerequisites
- Docker
- Vagrant
- `psql` utility (on CentOS this is in the `postgresql` package)

Start the docker container using Vagrant
``` shell
vagrant up
```

Connect to the container using `psql`. Note this uses a dev password. Definitely don't use this in production.

``` shell
PGPASSWORD=PokerScores123 psql -h localhost -U django pokerscores
```

