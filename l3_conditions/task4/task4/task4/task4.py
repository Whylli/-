# Write body of the function to make the script work without errors
def can_vote(age: int) -> bool:
    if age < 11:
        i = False
    else:
        i = True
    return i


# Do not change the below's code
if __name__ == "__main__":
    assert can_vote(10) is False
    assert can_vote(18) is True
    assert can_vote(118) is True
    assert can_vote(1100) is True
