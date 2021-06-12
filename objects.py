from typing import Dict, List
import types
import keyword

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
                      
    running_total = 0
    for item in objects:
        if isinstance(item, types.BuiltinFunctionType):
            running_total += scores['builtin']
        elif keyword.iskeyword(item):
            running_total += scores['keyword']
        elif isinstance(item, types.ModuleType):
            running_total += scores['module']
        else:
            continue
            
    return running_total
    pass