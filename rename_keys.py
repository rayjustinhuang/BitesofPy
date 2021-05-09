from typing import Dict, Any
from collections.abc import Iterable

def strip_at_signs(input_dict):
    new_keys = []
    
    for key in input_dict:
        if type(key) == str:
            key = key.replace('@', '')
            new_keys.append(key)
        else:
            new_keys.append(key)
    
    new_dict = dict(zip(new_keys, input_dict.values()))
        
    return new_dict
    
def dict_in_list(input_list):
    new_list = []
    
    for item in input_list:
        new_list.append(strip_at_signs(item))
        
    return new_list

def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    change = data.copy()
    
    new_dict = {}
    
    input_dict = strip_at_signs(change)
    
    for key, val in input_dict.items():
        if type(val) == dict:
            val = strip_at_signs(val)
            new_key = key.replace('@', '')
            new_dict[new_key] = val
            rename_keys(val)
        elif isinstance(val, list):
            print(val)
            new_key = key.replace('@', '')
            new_val = dict_in_list(val)
            new_dict[new_key] = new_val
        else:
            new_dict[key] = val
    
    return new_dict
    
test = {'@pii': {'@address': [{'@city': 'London'}, {'city': 'Moscow'}], '@email': 'jane@example.com', '@id': 12345, 'name': {'@first_name': 'Jane', '@last_name': 'Doe'}}}
test2 = {'@user_name': 'jdoe', 1: 'one', 2: 'two', '@three': 3}

print(rename_keys(test))