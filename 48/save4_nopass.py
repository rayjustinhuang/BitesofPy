import os
import urllib.request

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)

def create_chart():
    with open(LOG) as f:
        content = f.readlines()
        
    dates = [line.split()[0] for line in content]
    dates = sorted(dates, key=dates.index)
    print(dates)
    date_dict = {date : [] for date in dates}
    # print(date_dict)
    
    for i in range(0,len(content),2):
        bookline = content[i].split()
        slackline = content[i+1].split()
        if slackline[5] == 'sending':
            if 'python' in bookline or 'Python' in bookline:
                date_dict[bookline[0]].append(PY_BOOK)
            else:
                date_dict[bookline[0]].append(OTHER_BOOK)
    
    for key, value in date_dict.items():
        stringvalue = "".join(value)
        print(f'{key} {stringvalue}')
        #print(bookline)
        #print(slackline)
        #print()
    pass

create_chart()