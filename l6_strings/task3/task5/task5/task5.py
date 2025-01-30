# Write a function that returns True if string `s`
# has a prefix `prefix` and False otherwise.
#
# For example,
# 1. has_prefix("apple", "app") -> True
# 2. has_prefix("apple", "applg") -> False
def has_prefix(s: str, prefix: str) -> bool:
    if s == prefix:
        print("False")
        return False
    else:
        print("True")
        return True


# Do not change the below's code
if __name__ == "__main__":
    assert has_prefix("apple", "app") is True
    assert has_prefix("apple", "a") is True
    assert has_prefix("apple", "apple") is False
    assert has_prefix("", "") is True
