def flatten(list_of_lists):
    if list_of_lists == []:
        return list_of_lists
    elif type(list_of_lists[0]) == list:
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])

    return list_of_lists[:1] + flatten(list_of_lists[1:]) 
    
    pass