from typing import Dict, Any


def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    change = data.copy()
    
    for key in change:
        if type(key) == str:
            key.replace('@', '')
        else:
            continue
        
    return change