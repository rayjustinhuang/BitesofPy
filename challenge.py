from abc import ABC, abstractmethod


class Challenge(ABC):
    
    def __init__(self, number, title):
        self.number = number
        self.title = title
    pass

    @abstractmethod
    def verify(self, check):
        pass
    
    @property
    def pretty_title(self):
        return f'PCC{self.number} - {self.title}'
        pass


class BlogChallenge(Challenge):
    
    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, check):
        return check in self.merged_prs
        pass        

    @property
    def pretty_title(self):
        return f'PCC{self.number} - {self.title}'
        pass
    pass


class BiteChallenge(Challenge):
    
    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result
        
    def verify(self, check):
        return check == self.result
        pass        

    @property
    def pretty_title(self):
        return f'Bite {self.number}. {self.title}'
        pass
    pass