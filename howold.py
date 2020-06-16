from dataclasses import dataclass

from dateutil.relativedelta import relativedelta

from datetime import datetime


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    born_date = datetime.strptime(actor.born, '%B %d, %Y')
    movie_date = datetime.strptime(movie.release_date, '%B %d, %Y')
    
    diff = relativedelta(movie_date, born_date)
    
    age = diff.years
    
    return f'{actor.name} was {age} years old when {movie.title} came out.'
    pass