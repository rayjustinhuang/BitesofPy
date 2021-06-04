from typing import Dict, Any
from collections.abc import Iterable
import copy
from datetime import datetime

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
    
def dict_in_dict(input_dict):
    subsub_dict = {}
    for key, val in input_dict.items():
        subsub_key = key.replace('@', '')
        subsub_val = val
        subsub_dict[subsub_key] = subsub_val
        
    return subsub_dict, subsub_key

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
                            
                            subsub_dict = {}

                            for key3, val3 in item.items():
                                subsub_key = key3.replace('@', '')
                                subsub_val = val3

                                if type(subsub_val) == dict:
                                    subsubsub_dict = {}

                                    for key4, val4 in subsub_val.items():
                                        subsubsub_key = key4.replace('@', '')
                                        subsubsub_val = val4
                                        
                                        subsubsub_dict[subsubsub_key] = strip_at_signs(subsubsub_val)
                                
                                    subsub_dict[subsub_key] = subsubsub_dict
                                    
                                elif type(subsub_val) == list:

                                    subsub_dict[subsub_key] = dict_in_list(subsub_val)
                                    
                                else:
                                    # London and Moscow issue
                                    subsub_dict[subsub_key] = subsub_val
                            
                            new_val.append(strip_at_signs(subsub_dict))    
                            
                        else:
                            new_val.append(item)

                    sub_dict[sub_key] = new_val
                elif isinstance(val2, dict):
                    # sub_dict[sub_key] = strip_at_signs(val2)

                    subsub_dict = {}
                    for key3, val3 in val2.items():
                        subsub_key = key3.replace('@', '')
                        subsub_val = val3
                        subsub_dict[subsub_key] = subsub_val
                    
                        if isinstance(val3, dict):
                            subsubsub_dict = {}
                            for key4, val4 in val3.items():
                                subsubsub_key = key4.replace('@', '')
                                subsubsub_val = val4
                                subsubsub_dict[subsubsub_key] = subsubsub_val
                        
                            subsub_dict[subsub_key] = subsubsub_dict
                        
                    sub_dict[sub_key] = subsub_dict

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