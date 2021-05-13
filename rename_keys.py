from typing import Dict, Any
from collections.abc import Iterable
import copy

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
    change = copy.deepcopy(data)
    
    new_dict = {}
    
    input_dict = strip_at_signs(change)
    
    for key, val in input_dict.items():
        if type(val) == dict:
            new_key = key.replace('@', '')
            sub_dict = {}
            
            for key2, val2 in val.items():
                sub_key = key2.replace('@', '')
                if isinstance(val2, list):
                    new_val = []
                    for item in val2:
                        if type(item) == list:
                            new_val.append(dict_in_list(item))
                        elif type(item) == dict:
                            new_val.append(strip_at_signs(item))
                        else:
                            new_val.append(item)

                    sub_dict[sub_key] = new_val
                elif isinstance(val2, dict):
                    sub_dict[sub_key] = strip_at_signs(val2)
                else:
                    sub_dict[sub_key] = val2
                    
            sub_dict = strip_at_signs(sub_dict)
            
            new_dict[new_key] = sub_dict
                    
        elif isinstance(val, list):
            new_key = key.replace('@', '')
            new_val = dict_in_list(val)
            new_dict[new_key] = new_val
        else:
            new_dict[key] = val

    return new_dict
    
test = {'@pii': {'@address': [{'@city': 'London'}, {'city': 'Moscow'}], '@email': 'jane@example.com', '@id': 12345, 'name': {'@first_name': 'Jane', '@last_name': 'Doe'}}}
test2 = {'@user_name': 'jdoe', 1: 'one', 2: 'two', '@three': 3}
# print(iterdict(test))

print(rename_keys(test))