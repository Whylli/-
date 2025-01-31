# Use `for` loop to count all occurrence of character `c`
# in a string `s`.
def count_char(s: str, c: str) -> int:
    d = 0
    n = len(s)
    for i in range(n):
        if c == s[i]:
            d = d + 1
    return d


# Do not change the below's code
if __name__ == "__main__":
    assert count_char("ababa", "a") == 3
    assert count_char("ababa", "b") == 2
    assert count_char("ababa", "c") == 0
    assert count_char("cccca", "a") == 1
