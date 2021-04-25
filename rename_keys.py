from typing import Dict, Any

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

def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    change = data.copy()
    
    change = strip_at_signs(change)
    
    new_vals = []
    
    for val in change.values():
        if type(val) == dict:
            new_vals.append(strip_at_signs(val))
        else:
            new_vals.append(val)
            
    return dict(zip(change, new_vals))
    
test = {'@user_name': 'jdoe', 1: 'one', 2: 'two', '@three': 3}

print(rename_keys(test))