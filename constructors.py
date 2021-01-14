import re


class DomainException(Exception):
    """Raised when an invalid is created."""
    pass


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        if re.match(r'.*\.[a-z]{2,3}$', name) == None:
            raise DomainException
        # if not valid, raise a DomainException
        self.name = name
        
    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively
    def __str__(self):
        return self.name
    
    @classmethod
    def parse_url(self, name):
        if re.match(r'(https?:\/\/)([a-zA-Z0-9]+\.[a-z]{2,3})', name) == None:
            raise DomainException
        _, domain = re.match(r'(https?:\/\/)([a-zA-Z0-9]+\.[a-z]{2,3})', name).groups()
        self.name = domain
        #return domain
        pass
    
    @classmethod
    def parse_email(self, name):
        if re.match(r'.+@(.+\.[a-zA-Z]{2,3})', name) == None:
            raise DomainException
        domain = re.match(r'.+@(.+\.[a-zA-Z]{2,3})', name).groups()[0]
        self.name = domain
        #return domain
        pass
    
#str(Domain('google.com'))
#domain = Domain.parse_url("http://pybit.es")
#print(str(domain))
#domain2 = Domain.parse_email("julian@pybit.es")
#print(str(domain2))
#type(domain)
#print(re.match(r'.*\.[a-z]{2,3}$', 'nu.nlll'))