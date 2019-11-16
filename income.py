from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from collections import defaultdict

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    with open(xml) as f:
        content = f.read()
    
    income_dict = defaultdict(list)
    
    soup = BeautifulSoup(content, 'html.parser')
    
    for country in soup.find_all('wb:country'):
        income_dict[country.find('wb:incomelevel').text].append(country.find('wb:name').text)
        
    return income_dict
    pass