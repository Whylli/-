if __name__ == "__main__":
    l = [1, 5, 4]

    # Modify the value of variable `c` using
    # list `l` to make the script work without errors
    c = 0
    n = len(l)
    for i in range(n):
        c = c + l[i]
    print(c)


    # Do not change the below's code
    assert c == 10
