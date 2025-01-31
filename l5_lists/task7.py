def proxy_pop(l: list[int]) -> int:
    d = [0, 0, 0, 0]
    n = len(l)
    t = n
    for i in range(n):
        d[i] = l[t - i]
        return d[i]


# Do not change the below's code
if __name__ == "__main__":
    l = [3, 6, 1, 2]

    assert proxy_pop(l) == 2
    assert proxy_pop(l) == 1
    assert proxy_pop(l) == 6
    assert proxy_pop(l) == 3
