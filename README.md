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

Setup the project (did this already, but this is how i created the project

``` shell
django-admin startproject pokerscores
cd pokerscores/
python manage.py startapp leaderboard
```
