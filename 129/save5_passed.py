import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()

#print(data)
# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    else:
        no_dollar = cap.lstrip('$')
        if no_dollar[-1] == 'M':
            return float(no_dollar[:-1])
        else:
            return float(no_dollar[:-1])*1000
    pass

#print(_cap_str_to_mln_float('n/a'))
#print(_cap_str_to_mln_float('$100.45M'))
#print(_cap_str_to_mln_float('$1.52B'))


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    cap_values = 0
    for row in data:
        if row['industry'] == industry:
            cap_values += _cap_str_to_mln_float(row['cap'])
    return round(cap_values,2)
    pass

#print(get_industry_cap('Real Estate Investment Trusts'))

def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    stock_caps = {row['symbol'] : _cap_str_to_mln_float(row['cap']) for row in data}
    return max(stock_caps, key=stock_caps.get)
    pass

#print(get_stock_symbol_with_highest_cap())

def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors = Counter(row['sector'] for row in data if row['sector'] != 'n/a')
    return (sectors.most_common()[0][0], sectors.most_common()[-1][0])
    pass

#get_sectors_with_max_and_min_stocks()