import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    pattern = r'([0-9]{2}\:[0-9]{2})'
    times = re.findall(pattern, course)
    return times
    pass


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    #pattern = r'(#{1}[^\s]{2,})'
    #hashtags = re.findall(pattern, tweet)
    #pattern2 = r'(http:\/\/[a-z0-9]+\.[^\s]{2,})'
    #links = re.findall(pattern2, tweet)
    both = r'(#{1}[^\s]{2,})|(http:\/\/[a-z0-9]+\.[^\s]{2,})'
    x = re.findall(both, tweet)
    hashtags_and_links = []
    for tup in x:
        hashtags_and_links+=[i for i in tup if i != '']
    return hashtags_and_links
    pass


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    pattern = r'<p>?([^<]+)?<\/p>?'
    paras = re.findall(pattern, html)[0]
    return paras
    pass