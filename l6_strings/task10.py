# Write a function that returns True if
# the first character of the string `s`
# equals the last character of the string `s`;
# return False otherwise
def same_chars(s: str) -> bool:
    x = len(s)
    i = 0
    x = x - 1
    k = 0
    while x - i >= i:
        if s[x - i] == s[i]:
            i += 1
        else:
            k = 1
            break
    if k == 1:
        return False
    else:
        return True


# Do not change the below's code
if __name__ == "__main__":
    assert same_chars("abba") is True
    assert same_chars("Abba") is False
    assert same_chars("baba") is False
    assert same_chars("cabac") is True
