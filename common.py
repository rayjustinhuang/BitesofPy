def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
       
    names = programmers.keys()
    
    common = set()
    
    for name in names:
        check = common.intersection(set(programmers[name]))
        common.update(check)
        
    return common
    pass