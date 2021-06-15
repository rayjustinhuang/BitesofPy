from typing import Dict, List
import types
import keyword
import inspect
import builtins
import sys

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
                      
    running_total = 0
    for item in objects:
        if item in dir(builtins):
            running_total += scores['builtin']
        elif keyword.iskeyword(item):
            running_total += scores['keyword']
        elif item in sys.builtin_module_names:
            running_total += scores['module']
        else:
            continue
            
    return running_total
    pass

test = ['raise', 'random']
test2 = ['any', 'all', 'max']

print(score_objects(test, scores))

print(isinstance('random', types.ModuleType))