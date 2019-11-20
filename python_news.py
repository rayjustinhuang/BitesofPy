from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    # you code
    titles = soup.find_all('span', class_='title')
    points = soup.find_all('span', class_='controls')
    
    title_list = []
    
    for title, point in zip(titles, points):
        p = int(point.find('span', class_='smaller').text.strip().split()[0])
        c = int(point.find('span', class_='smaller').text.strip().split()[-2])
        
        if title.find('span',class_='smaller') == None:
            t = title.find('a').text
            title_list.append(Entry(t, p, c))
            continue
        
        t = title.find('a').text + " " + title.find('span', class_='smaller').text
        
        title_list.append(Entry(t, p, c))
        
    return sorted(title_list, key = lambda x: (x[1], x[2]), reverse=True)[:top]