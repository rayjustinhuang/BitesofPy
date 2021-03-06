NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    outlist = list(set(names))
    final = [name.title() for name in outlist]
    return final
    pass


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    secondname = lambda elem: elem.split(" ",2)[1]
    final = sorted(names, key=secondname, reverse=True)
    return final
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    firstname = lambda elem: elem.split(" ",1)[0]
    givennames = [firstname(name) for name in names]
    print(givennames)
    final = sorted(givennames, key=len)
    print(final)
    return final[0]
    # ...