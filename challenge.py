from abc import ABC, abstractmethod


class Challenge(ABC):
    
    def __init__(self, number, title):
        self.number = number
        self.title = title
    pass

    @abstractmethod
    def verify(self):
        pass
    
    @property
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):
    pass


class BiteChallenge(Challenge):
    pass