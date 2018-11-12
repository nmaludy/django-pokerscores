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
 - Activity (tournaments played)
 
Season
 - name
 - League
 - start date
 - end date
 - List[Tournament]
 - active
 - visible
 
Tournament
 - name
 - start date
 - end date
 - League
 - Optional[Season]
 - List[Score]
 - ScoringSystem
 
Score
 - Player
 - points
 - Game
 
ScoringSystem
 - name
 - List[int] - points per place

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
python manage.py startapp leaderboard
```

Initialize the database

``` shell
python manage.py migrate
```

Run the test server (dev only)

``` shell
python manage.py runserver
```

Test out the site by going to [http://localhost:8000/leaderboard](http://localhost:8000/leaderboard)
