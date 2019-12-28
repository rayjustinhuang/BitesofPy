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
    
    def __init__(self, merged_prs):
        super().__init__(args)
        self.merged_prs = merged_prs
    pass


class BiteChallenge(Challenge):
    
    def __init__(self, result):
        super().__init__(args)
        self.result = result
    pass