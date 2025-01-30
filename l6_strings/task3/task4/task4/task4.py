# Write a function that returns `max(len(s), n)`
# characters from the middle of the string.
#
# For example,
# 1. middle("abddcvbn", 4) -> "ddcv"
# 2. middle("abddcvbn", 3) -> "ddc"
#
# NOTE: use // division to define slice start index
def middle(s: str, n: int) -> str:
    t = ""
    if n <= 0:
        return ""
    if n >= len(s):
        return s
    else:
        for i in range(n):
            t = t + s[i + 2]
        return t


# Do not change the below's code
if __name__ == "__main__":
    assert middle("abddcvbn", 4) == "ddcv"
    assert middle("abddcvbn", 3) == "ddc"
    assert middle("dcd", 5) == "dcd"
    assert middle("", 10) == ""
