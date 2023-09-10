from typing import Any
import math
import collections


def _floor(x: float) -> int:
    return int(x)


def _nroot(n: int, x: int) -> int:
    return math.pow(x, 1 / n)


def _reverse(s: str) -> str:
    s_reversed = "".join(list(reversed(s)))
    return s_reversed


def _validAnagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    map1 = collections.defaultdict(lambda: 0)
    map2 = collections.defaultdict(lambda: 0)
    for c1, c2 in zip(s1, s2):
        map1[c1] += 1
        map2[c2] += 1
    return map1 == map2


def _sort(strArr: list[str]) -> list[str]:
    strArr_reversed = list(sorted(strArr))
    return strArr_reversed


METHOD_TO_CALLABLE = {
    "floor": _floor,
    "nroot": _nroot,
    "reverse": _reverse,
    "validAnagram": _validAnagram,
    "sort": _sort,
}

METHOD_TO_PARAM_TYPES = {
    "floor": ["float"],
    "nroot": ["int", "int"],
    "reverse": ["str"],
    "validAnagram": ["str", "str"],
    "sort": ["list[str]"],
}


def executeRpcFunction(json_data: dict[str, Any]) -> dict[str, Any]:
    """
    request sample
    {
       "method": "subtract",
       "params": [42, 23],
       "param_types": ["int", "int"],
       "id": 1
    }
    response sample
    {
       "results": "19",
       "result_type": "int",
       "id": 1
    }
    """
    try:
        method = json_data["method"]
        params = json_data["params"]
        param_types = json_data["param_types"]
        id = json_data["id"]
        # print(f"method -> {method}")
        # print(f"param_types -> {param_types}")
        if METHOD_TO_PARAM_TYPES[method] != param_types:
            return {"error": "'param_types' is invalid"}
        result = METHOD_TO_CALLABLE[method](*params)
        resp_data = {}
        resp_data["results"] = result
        resp_data["result_type"] = str(type(result)).split("'")[1]
        resp_data["id"] = id
        return resp_data
    except Exception as e:
        print(str(e))
        return {"error": str(e)}
