from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    
    def __init__(self, name):
        self.name = name
        self._transactions = []

    @property
    def points(self):
        return [transaction.points for transaction in self._transactions]
    
    @property    
    def karma(self):
        return sum(self.points)
        
    @property
    def fans(self):
        return len(set([transaction.giver for transaction in self._transactions]))
        
    def __add__(self, transaction):
        return self._transactions.append(transaction)
        pass
    
    def __str__(self):
        if self.fans == 1:
            return f'{self.name} has a karma of {self.karma} and {self.fans} fan'
        else:
            return f'{self.name} has a karma of {self.karma} and {self.fans} fans'
    
    pass