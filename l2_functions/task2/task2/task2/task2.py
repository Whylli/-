# Declare a function named `join`
# that accepts two strings as parameters
# and returns their concatenation separated
# by whitespace ' '.
#
# For example, call of `join("a", "b")` should return "a b"


# Do not change the below's code
if __name__ == "__main__":
    a, b = "Jon", "Doe"
    abb[0] = a
    abb[1] = b
    ab = ' '.join(abb)
    print(ab)

    assert join(a, b) == "Jon Doe"
    assert join(b, a) == "Doe Jon"
    assert join("aba", "baba") == "aba baba"
