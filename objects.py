from typing import Dict, List
import types
import keyword
import inspect
import builtins
import importlib

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
                      
    running_total = 0
    for item in objects:
        try:
            importlib.import_module(item)
            running_total += scores['module']
        except:
            if item in dir(builtins) and keyword.iskeyword(item):
                running_total += scores['builtin'] + scores['keyword']
            elif item in dir(builtins):
                running_total += scores['builtin']
            elif keyword.iskeyword(item):
                running_total += scores['keyword']
            else:
                continue
            
    return running_total
    pass