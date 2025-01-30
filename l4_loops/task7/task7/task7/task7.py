# Use `while` loop to calculate the number
# of digits in a number `n`
def count_digits(n: int) -> int:
    s = 1
    while n >= 0:
        n = n / 10
        s = s + 1
    return s


# Do not change the below's code
if __name__ == "__main__":
    assert count_digits(0) == 1
    assert count_digits(134) == 3
    assert count_digits(54) == 2
    assert count_digits(55678) == 5
