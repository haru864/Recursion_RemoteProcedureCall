from typing import Any
import math
import collections


def floor(x: float) -> int:
    return int(x)


def nroot(n: int, x: int) -> int:
    return math.pow(x, 1 / n)


def reverse(s: str) -> str:
    s_reversed = "".join(list(reversed(s)))
    return s_reversed


def validAnagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    map1 = collections.defaultdict(lambda: 0)
    map2 = collections.defaultdict(lambda: 0)
    for c1, c2 in zip(s1, s2):
        map1[c1] += 1
        map2[c2] += 1
    return map1 == map2


def sort(strArr: list[str]) -> list[str]:
    strArr_reversed = list(sorted(strArr))
    return strArr_reversed


METHOD_TO_CALLABLE = {
    "floor": floor,
    "nroot": nroot,
    "reverse": reverse,
    "validAnagram": validAnagram,
    "sort": sort,
}

METHOD_TO_PARAM_TYPES = {
    "floor": ["float"],
    "nroot": ["int", "int"],
    "reverse": ["str"],
    "validAnagram": ["str", "str"],
    "sort": ["list[str]"],
}


def executeRpcFunction(
    method: str, params: list[Any], param_types: list[str]
) -> dict[str, str]:
    try:
        if METHOD_TO_PARAM_TYPES[method] != param_types:
            return {"error": "'param_types' is invalid"}
        result = METHOD_TO_CALLABLE[method](*params)
        resp_data = {}
        resp_data["results"] = result
        resp_data["result_type"] = str(type(result)).split("'")[1]
        return resp_data
    except Exception as e:
        print(str(e))
        return {"error": str(e)}
