def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
       
    names = list(programmers.keys())
    
    languages = sorted(list(programmers.values()), key = lambda x: len(x))
    
    common = set(languages[0]).intersection(set(languages[1]))
    
    for name in names:
        check = common.intersection(set(programmers[name]))
        common.update(check)
        
    return list(common)
    pass

programmers = dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'], sue=['Scala','Python'])
                
print(common_languages(programmers))