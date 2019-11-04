from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()

#print(data[0]['automaker'])

# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automakers = []
    relevant_data = []
    for i in range(len(data)):
        if data[i]['year'] == year:
            relevant_data.append(data[i])

    for i in range(len(relevant_data)):
        automakers.append(relevant_data[i]['automaker'])
    automaker_count = Counter(automakers)
    return automaker_count.most_common(1)[0][0]
    pass


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    relevant_data = []
    for i in range(len(data)):
        if data[i]['automaker'] == automaker:
            if data[i]['year'] == year:
                relevant_data.append(data[i])
                
    relevant_models = []
    for j in range(len(relevant_data)):
        relevant_models.append(relevant_data[i]['automaker'])
    return set(relevant_models)
    pass

# most_prolific_automaker(1999)
# print(get_models('Dodge', 1999))