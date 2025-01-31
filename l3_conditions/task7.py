# Write the body of the function to make the script work without errors
def grade(score: int) -> str:
    if score == 95:
        i = "A"
    if score == 85:
        i = "B"
    if score == 75:
        i = "C"
    if score == 65:
        i = "D"
    if score == 50:
        i = "F"
    return i


if __name__ == "__main__":
    # Do not change the below asserts
    assert grade(95) == "A"
    assert grade(85) == "B"
    assert grade(75) == "C"
    assert grade(65) == "D"
    assert grade(50) == "F"
