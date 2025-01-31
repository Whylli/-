# Import the function `ceil` from package `math` to make the script work without errors
def ceil(n):
    if n > int(n):
        n = int(n) + 1
        print(n)
        return n
    else:
        print(n)
        return n
# Do not modify the code below
if __name__ == "__main__":
    assert ceil(4.1) == 5
