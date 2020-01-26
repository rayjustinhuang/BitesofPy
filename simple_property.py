from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires
    
    @property
    def expired(self):
        if NOW > self.expires:
            return True
        else:
            return False
    pass