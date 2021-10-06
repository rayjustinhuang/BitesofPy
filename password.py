import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if not 12 >= len(password) >= 6:
        return False
    
    if sum(x.isdigit() for x in password) < 1:
        return False
        
    if sum(x.islower() for x in password) < 2:
        return False
        
    if sum(x.isupper() for x in password) < 1:
        return False
    pass