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
    
def iterdict(input_dict):
    new_dict = {}
    
    input_dict = strip_at_signs(input_dict)
    
    for key, val in input_dict.items():
        if type(val) == dict:
            val = strip_at_signs(val)
            new_key = key.replace('@', '')
            new_dict[key] = val
        elif isinstance(val, Iterable):
            for obj in val:
                if type(obj) == dict:
                    obj = strip_at_signs(obj)
        else:
            new_dict[key] = val
        iterdict(val)
    
    return new_dict

def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    change = data.copy()
    
    change = strip_at_signs(change)
    
    iterdict(change)
            
    return change
    
test = {'@pii': {'@address': [{'@city': 'London'}, {'city': 'Moscow'}], '@email': 'jane@example.com', '@id': 12345, 'name': {'@first_name': 'Jane', '@last_name': 'Doe'}}}

print(iterdict(test))

print(rename_keys(test))