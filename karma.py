from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    
    def __init__(self, name):
        self.name = name
        self.transactions = []

    @property
    def points(self):
        return [transaction.points for transaction in self.transactions]
    
    @property    
    def karma(self):
        return sum(self.points)
        
    @property
    def fans(self):
        return [transaction.giver for transaction in self.transactions]
        
    def __add__(self, transaction):
        return self.transactions.append(transaction)
        pass
    
    def __str__(self):
        if len(self.fans) == 1:
            return f'{self.name} has a karma of {self.karma} and {len(self.fans)} fan'
        else:
            return f'{self.name} has a karma of {self.karma} and {len(self.fans)} fans'
    
    pass