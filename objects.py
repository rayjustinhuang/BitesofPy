from typing import Dict, List
import types
import keyword
import inspect
import builtins
import sys
import pkg_resources

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
                      
    installed_packages = pkg_resources.working_set
    installed_packages_list = ["%s" % (i.key) for i in installed_packages]
                      
    running_total = 0
    for item in objects:
        if item in installed_packages_list:
            running_total += scores['module']
        elif item in dir(builtins):
            running_total += scores['builtin']
        elif keyword.iskeyword(item):
            running_total += scores['keyword']
        else:
            continue
            
    return running_total
    pass

test = ['raise', 'random']
test2 = ['any', 'all', 'max']

#print(score_objects(test, scores))

#print(isinstance('random', types.ModuleType))

#help('modules')