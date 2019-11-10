from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    games = []
    stream = feedparser.parse(FEED_URL)
    for game in stream.entries:
        games.append(Game(title=game.title, link=game.link))
    return games
    pass