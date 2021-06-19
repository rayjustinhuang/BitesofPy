from typing import Dict, List
import types
import keyword
import inspect
import builtins
import sys
import pkg_resources
import pip

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
                      
    installed_packages = pip.get_installed_distributions(local_only=True)
    installed_packages_list = ["%s" % (i.key) for i in installed_packages]
                      
    running_total = 0
    for item in objects:
        if item in installed_packages:
            running_total += scores['module']
        elif item in dir(builtins):
            running_total += scores['builtin']
        elif keyword.iskeyword(item):
            running_total += scores['keyword']
        else:
            continue
        
        print(item, running_total)    
    return running_total
    pass

test = ['raise', 'random']
test2 = ['any', 'all', 'max']

print(score_objects(test, scores))

#print(isinstance('random', types.ModuleType))

#help('modules')


