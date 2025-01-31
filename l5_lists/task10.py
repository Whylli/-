from typing import Any


# Write the function that reverses the list `l`
# NOTE: the function must create a new list.
# Do not modify list `l`.
def reverse(l: list[Any]) -> list[Any]:
    d = [0, 0, 0]
    n = len(l)
    t = n - 1
    for i in range(n):
        d[i] = l[t]
        t = t - 1
    return d


# Do not change the below's code
if __name__ == "__main__":
    l = [3, 4, 5]

    assert reverse(l) == [5, 4, 3]
    assert l == [3, 4, 5]

    assert reverse(["c", "b", "a"]) == ["a", "b", "c"]
