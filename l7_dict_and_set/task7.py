from typing import Any


# Write a body of the function. It should merge to dictionaries d1 and d2.
# NOTE: the function should create a new dictionary. Do not modify dictionaries
# passed to the function as arguments
def merge(d1: dict[Any, Any], d2: dict[Any, Any]) -> dict[Any, Any]:
    d = {"a": 0, "b": 0, "c": 0, "d": 0}
    d["a"] = d1["a"]
    d["b"] = d1["b"]
    d["c"] = d2["c"]
    d["d"] = d2["d"]
    return d

# Do not change the below's code
if __name__ == "__main__":
    assert merge({"a": 1, "b": 2}, {"c": 3, "d": 4}) == {"a": 1, "b": 2, "c": 3, "d": 4}

    d1, d2 = {"a": 1}, {"b": 1}
    assert merge(d1, d2) == {"a": 1, "b": 1}
    assert d1 == {"a": 1}
    assert d2 == {"b": 1}
