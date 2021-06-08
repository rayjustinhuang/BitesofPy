import json
from pathlib import Path
from urllib.request import urlretrieve
import pandas as pd

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
TMP = Path('/tmp')

def get_data(file_no=1, tmp=TMP):
    file_name = f'bite_scores{file_no}.json'
    file_path = TMP / file_name
    remote = 'https://bites-data.s3.us-east-2.amazonaws.com/'
    if not file_path.exists():
        urlretrieve(f'{remote}{file_name}',
                    file_path)
    return file_path

def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    #print(data)
    with open(data) as f:
        json_data = json.load(f)
    
    df = pd.DataFrame(json_data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['date'])
    
    df['cumsum'] = df['score'].cumsum()
    
    # reverse_df = df.sort_values(by=['date'], ascending = False)
    prev_cumsum = 0
    final_dict = {}
    active_belt = 0
    for index, row in df.iterrows():
        active_score = row['cumsum']
        
        if active_score >= SCORES[active_belt] and prev_cumsum < SCORES[active_belt]:
            final_dict[BELTS[active_belt]] = row['date']
            active_belt += 1
        
        prev_cumsum = row['cumsum']
    
    return final_dict
    pass

data = get_data()
get_belts(data)