from collections import Counter, defaultdict
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join('/tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    with open(commits) as f:
        log = f.read().splitlines()
    
    changes_dict = defaultdict(int)
    
    for row in log:
        datetime_string = row.split()[1:7]
        datetimes = parse(" ".join(datetime_string))
        yearmonth = YEAR_MONTH.format(y=datetimes.year, m=datetimes.month)
        if year != None:
            if datetimes.year != year:
                continue
        
        changes_string = row.split()[11:]
        for item in changes_string:
            if item.isnumeric():
                changes_dict[yearmonth] += int(item)
    
    return (min(changes_dict, key=changes_dict.get), max(changes_dict, key=changes_dict.get))
    pass

print(get_min_max_amount_of_commits())