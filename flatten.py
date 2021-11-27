def flatten(list_of_lists):
    if list_of_lists == []:
        return list(list_of_lists)
    elif type(list_of_lists[0]) == list or type(list_of_lists[0]) == tuple:
        return flatten(list(list_of_lists[0])) + flatten(list(list_of_lists[1:]))

    return list(list_of_lists[:1]) + flatten(list(list_of_lists[1:])) 
    
    pass