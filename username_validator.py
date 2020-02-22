# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re
from itertools import islice

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    platforms_raw_list = social_platforms.splitlines()
    raw_list_to_split = iter(platforms_raw_list)
    number_to_split_on = platforms_raw_list.index("") + 1
    number_of_sublists = platforms_raw_list.count("") + 1
    length_to_split = [number_to_split_on]*number_of_sublists
    print(length_to_split)
    split_string = [list(islice(raw_list_to_split, length)) for length in length_to_split]
    print(split_string)
    pass

parse_social_platforms_string()

def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    # ...