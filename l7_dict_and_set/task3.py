if __name__ == "__main__":
    # Do not modify the line below
    a, b = {"a", "b", "c", "d"}, {"a", "b", "n", "m"}

    # Use sets `a` and `b` to modify a value of `c` to make the script
    # work without errors.
    # `c` should contain a union of `a` and `b`
    c = None
    ñ = b["a"]
    ñ = b["a"]
    ñ = b["b"]
    ñ = a["c"]
    ñ = a["d"]
    ñ = b["n"]
    ñ = b["m"]

    # Do not modify the line below
    assert c == {"a", "b", "c", "d", "n", "m"}
