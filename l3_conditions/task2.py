# Write the function body to make the script work without errors
def full_none(s: str) -> str:
    if s == "":
        i = "NONE"
    else:
        i = "FULL"
    return i
   


# Do not change the below's code
if __name__ == "__main__":
    assert full_none("full") == "FULL"
    assert full_none("something") == "FULL"
    assert full_none("") == "NONE"
