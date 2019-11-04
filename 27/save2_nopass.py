import glob
import json
import os
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movie_dicts = []
    for item in files:
        with open(item,'r') as f:
            movie_dicts.append(json.load(f))
    return movie_dicts
    pass

#movies = get_movie_data(files)
#for movie in movies:
#    print(type(movie))
#print(len(movies))

def get_single_comedy(movies):
    return [row['Title'] for row in movies if 'Comedy' in row['Genre']][0]
    pass

# print(get_single_comedy(get_movie_data(files)) == 'Horrible Bosses')

def get_movie_most_nominations(movies):
    nominations = dict(zip([row['Title'] for row in movies], [int(row['Awards'].split()[-2]) for row in movies]))
    return max(nominations, key=nominations.get)
    pass

# print(get_movie_most_nominations(movies))

def get_movie_longest_runtime(movies):
    runtimes = dict(zip([row['Title'] for row in movies], [int(row['Runtime'].split()[-2]) for row in movies]))
    return max(runtimes, key=runtimes.get)
    pass

#print(get_movie_longest_runtime(movies))