from collections import Counter

import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    req = requests.get(url)
    
    soup = bs4.BeautifulSoup(req.content, 'html.parser')
    
    #print(soup)
    
    emails = soup.find_all('div', TARGET_DIV)[0].find_all('img')
    
    domain_list = [line.get('src').split('=')[-1] for line in emails]
    
    return domain_list
    pass


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    # your code
    given_domains = [item.split('@')[-1] for item in emails]
    
    result_count = Counter(given_domains)
    
    return [i for i in filter(lambda x: x[0] not in common_domains, result_count.items())]