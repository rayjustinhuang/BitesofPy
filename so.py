import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    content = requests.get(url).content
    
    soup = BeautifulSoup(content, 'html.parser')
    
    questions = soup.find_all('div', class_='question-summary')
    
    question_list = []
    
    for q in questions:
        question = q.find('a', class_='question-hyperlink').text
        votes = int(q.find('span', class_='vote-count-post').text)
        views = q.find('div', class_='views').text.strip()
        
        if views.split()[0][-1] == 'k':
            continue
        
        #views = float(views.split()[0][:-1])
        
        question_list.append((question, votes))
        
    return sorted(question_list, key=lambda x: x[1], reverse=True)
    pass