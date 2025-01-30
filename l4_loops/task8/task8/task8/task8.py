# Use `for` loop to calculate the amount
# of positive number in a list of integers `n`
def count_positive(n: list[int]) -> int:
    r = len(n)
    t = 0
    for i in range(r):
        if n[i] >= 0:
            t = t + 1
    return t


# Do not change the below's code
if __name__ == "__main__":
    assert count_positive([1, 2, -3, -4]) == 2
    assert count_positive([-1, -2, -3]) == 0
    assert count_positive([4, 5, 4, 3]) == 4
