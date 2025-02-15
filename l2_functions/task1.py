Number = int | float | complex


# Write the body of the function to make the script
# work without errors
def sqr(n: Number) -> Number:
    pass


if __name__ == "__main__":
    a = 4
    b = 4.0
    c = 5
    d = 12
    # Do not change the below asserts
    assert sqr(2) == 4
    assert sqr(4.0) == 16
    assert sqr(3 + 2j) == 5 + 12j
