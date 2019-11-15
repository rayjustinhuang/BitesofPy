from collections import Counter

from bs4 import BeautifulSoup
import requests
import re

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()
    # code here ...
    soup = BeautifulSoup(content, 'html.parser')
    
<<<<<<< HEAD
    links = soup.find_all('a', href=re.compile(AMAZON))
    
    c = Counter([(title, title.text) for title in links])
    
    return [book[0][1] for book in c.most_common(limit)]
=======
    c = Counter()
    
    links = soup.find_all('a', href=re.compile(AMAZON))
    
    for title in links:
        c[title.text] += 1
    
    return [book[0] for book in c.most_common(limit)]
>>>>>>> a6ba49e3432ffade53d1a76f38b21949c00a9883
