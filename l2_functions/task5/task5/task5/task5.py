# Declare and write the body of the function named `count_params`.
# The function should accept arbitrary amount of arguments and
# you should return the amount of passed arguments.
#
# HINT:
# Use *

def count_params(a, b, c, d):
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    i = len(a) 
    i = i + len(b)
    i = i + len(c)
    i = i + len(d)
    return i

# Do not change the below's code
if __name__ == "__main__":
    assert count_params(1, 2, 3, 4) == 4
    assert count_params(3, "asd", (3, 4, 5)) == 3
