if __name__ == "__main__":
    # Do not change the line below
    l = [1, 2, 5, 0, -3]

    # Modify variable c using list l to make this script work without errors
    c = [0, 0]
    c[0] = l[0]
    c[1] = l[1]
    print(c[0])
    print(c[1])

    # Do not change the line below
    assert c == [1, 2]
