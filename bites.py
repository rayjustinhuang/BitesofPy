import csv
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    
    with open(stats) as f:
        csv_reader = csv.reader(f, delimiter=";")
        bites_list = [row for row in csv_reader]

    bites_list.pop(0)
    
    n = N
    if len(bites_list) < N:
        n = max(N, len(bites_list))
    
    for bite in bites_list:
        if len(bite) == 1:
            bite.append(0)
        bite.append(bite[0].split(" ")[1][:-1])

        if bite[1] == 'None':
            bite[1] = 0
        else:
            bite[1] = float(bite[1])
    
    return [number[2] for number in sorted(bites_list, key=lambda m: m[1], reverse=True)[:n]]
    pass


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)