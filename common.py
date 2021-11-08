def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
       
    names = list(programmers.keys())
    
    common = set(programmers[names[0]]).intersection(set(programmers[names[1]]))
    
    for name in names:
        check = common.intersection(set(programmers[name]))
        common.update(check)
        
    return common
    pass

programmers = dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'])
                
print(common_languages(programmers))