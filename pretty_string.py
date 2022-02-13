import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    result = pprint.pp(obj, depth = 2, width = 60)
    return result
    pass