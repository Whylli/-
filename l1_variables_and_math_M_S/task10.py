if __name__ == "__main__":
    # Do not change the line below
    l = [1, 2, 5, 0, -3]

    # Modify variable c using list l to make this script work without errors
    c = [0, 0, 0, 0, 0]
    for i in range(5):
        y = 4 - i
        c[i] = l[y]
        print(c[i])

    # Do not change the line below
    assert c == [-3, 0, 5, 2, 1]
