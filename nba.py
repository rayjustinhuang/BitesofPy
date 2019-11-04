from collections import namedtuple
import csv
from pathlib import Path
import sqlite3

import requests

DATA_URL = 'https://query.data.world/s/ezwk64ej624qyverrw6x7od7co7ftm'
TMP = Path('/tmp')
DB = TMP / 'nba.db'

Player = namedtuple('Player', ('name year first_year team college active '
                               'games avg_min avg_points'))

conn = sqlite3.connect(DB)
cur = conn.cursor()


def import_data():
    with requests.Session() as session:
        content = session.get(DATA_URL).content.decode('utf-8')

    reader = csv.DictReader(content.splitlines(), delimiter=',')

    players = []
    for row in reader:
        players.append(Player(name=row['Player'],
                              year=row['Draft_Yr'],
                              first_year=row['first_year'],
                              team=row['Team'],
                              college=row['College'],
                              active=row['Yrs'],
                              games=row['Games'],
                              avg_min=row['Minutes.per.Game'],
                              avg_points=row['Points.per.Game']))

    cur.execute('''CREATE TABLE IF NOT EXISTS players
                  (name, year, first_year, team, college, active,
                  games, avg_min, avg_points)''')
    cur.executemany('INSERT INTO players VALUES (?,?,?,?,?,?,?,?,?)', players)
    conn.commit()


if DB.stat().st_size == 0:
    print('loading data')
    import_data()


# you code:

def player_with_max_points_per_game():
    """The player with highest average points per game (don't forget to CAST to
       numeric in your SQL query)"""
    return cur.execute("SELECT name FROM players WHERE CAST(avg_points AS numeric)=(SELECT MAX(CAST(avg_points AS numeric)) FROM players)").fetchone()[0]
    pass

#print(player_with_max_points_per_game())

def number_of_players_from_duke():
    """Return the number of players with college == Duke University"""
    return cur.execute("SELECT COUNT(DISTINCT name) from players where college='Duke University'").fetchone()[0]
    pass

#print(number_of_players_from_duke())

def avg_years_active_players_stanford():
    """Return the average years that players from "Stanford University
       are active ("active" column)"""
    return cur.execute("SELECT ROUND(AVG(active), 2) FROM players WHERE college='Stanford University'").fetchone()[0]
    pass

#print(avg_years_active_players_stanford())

def year_with_most_drafts():
    """Return the year with the most drafts, in SQL you can use GROUP BY"""
    return cur.execute("""SELECT year, MAX(drafts) FROM (SELECT year, COUNT(year) as drafts FROM players GROUP BY year) as year_table""").fetchone()[0]
    pass

#print(year_with_most_drafts())