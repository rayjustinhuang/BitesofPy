from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.karma = 0
        
    def __add__(self, transaction):
        pass
    
    pass