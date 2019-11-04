import os
import urllib.request

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)

def create_chart():
    with open(LOG) as f:
        for line in f.readlines():
            next_line = next(f.readlines())
            print(line[5:])
            print(next_line[6])
    pass

create_chart()