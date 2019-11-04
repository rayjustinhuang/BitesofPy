from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')

#print(get_season_csv_file(season=1))

def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    content_by_line = content.splitlines()
    
    # print(content_by_line)
    
    content_csv = csv.DictReader(content_by_line)
    # rows: Season, Episode, Character, Line
    
    counter_dict = defaultdict(Counter)
    
    for row in content_csv:
        if row['Episode'] == 8 and row['Character'] == 'Agent 1':
            print(row['Line'])
            print(len(row['Line'].split()))
        counter_dict[row['Character']][row['Episode']] = len(row['Line'].split())
    return dict(counter_dict)
    pass

content = get_season_csv_file(season=1)

print(get_num_words_spoken_by_character_per_episode(content)['Agent 1'])