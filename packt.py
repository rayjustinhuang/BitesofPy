from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    
    title = soup.h2.string.strip() #title
    
    dotd = soup.find('div', class_='dotd-main-book-summary float-left')
    
    description = dotd.find_all('div')[2].string.strip()
    image = soup.find('img', class_='bookimage imagecache imagecache-dotd_main_image').get('src')
    link = soup.find('div', class_='dotd-main-book-image float-left').a.get('href')
    
    return Book(title, description, image, link)
    pass