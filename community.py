import csv

import requests

from collections import Counter

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    response = requests.get(CSV_URL)
    
    csv_reader = csv.reader(response.text.splitlines(), delimiter=',')
    
    next(csv_reader)
    
    return csv_reader
    pass


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    country_count = Counter(row[2] for row in content)
    country_count = sorted(country_count.items(), key=lambda x: x[0])
    
    str_to_return = ''
    
    for row in country_count:
        str_to_return += row[0]
        str_to_return += ' '*(21-len(row[0]))
        str_to_return += '| '
        str_to_return += '+'*row[1]
        str_to_return += '\n'
    
    return str_to_return.splitlines()
    pass