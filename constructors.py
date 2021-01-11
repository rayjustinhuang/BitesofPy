import re


class DomainException(Exception):
    """Raised when an invalid is created."""
    pass


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        try:
            re.match(r'.*\.[a-z]{2,3}$', name)
        except:
            raise DomainException
        # if not valid, raise a DomainException
        self.name = name
        
    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively
    def __str__(self):
        return self.name
    
    def parse_from_url(self, url):
        try:
            re.match(r'(https?:\/\/)([a-zA-Z0-9]+\.[a-z]{2,3})', url)
        except:
            raise DomainException
        _, domain = re.match(r'(https?:\/\/)([a-zA-Z0-9]+\.[a-z]{2,3})', url)
        self.name = domain
        pass
    
    def parse_from_email(self):
        pass