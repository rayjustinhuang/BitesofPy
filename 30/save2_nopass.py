import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = []
    useful_rows = []
    with open(MOVIE_DATA, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        # director name: 1; movie_title: 11; title_year: 23; imdb_score: 25
        next(csv_reader)
        for row in csv_reader:
            if row[23] != "":
                directors.append(row[1])
                useful_rows.append([row[1],row[11].replace('\xa0',''),int(row[23]),float(row[25])])
    
    directors = set(director for director in directors[1:] if director != "")
        
    dict_of_directors = {director : [] for director in directors}
    
    # print(useful_rows)
    
    for director in dict_of_directors.keys():
        for row in useful_rows:
            # print(row[23])
            if row[0] == director and row[2] > MIN_YEAR:
                dict_of_directors[director].append(Movie(row[1],row[2],row[3]))
    #print(dict_of_directors['Woody Allen'])
    return dict_of_directors
    pass

directors = get_movies_by_director()

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = [movie.score for movie in movies]
    return round(mean(scores),1)
    pass


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    for director in directors.keys():
        if len(directors[director]) >= MIN_MOVIES:
            print(director)
    pass

get_average_scores(directors)