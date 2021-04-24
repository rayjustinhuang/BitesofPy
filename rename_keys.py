from typing import Dict, Any


def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    change = data.copy()
    
    new_keys = []
    
    for key in change:
        if type(key) == str:
            key = key.replace('@', '')
            new_keys.append(key)
        else:
            new_keys.append(key)
    
    new_dict = dict(zip(new_keys, change.values()))
        
    return new_dict
    
test = {'@user_name': 'jdoe', 1: 'one', 2: 'two', '@three': 3}

print(rename_keys(test))