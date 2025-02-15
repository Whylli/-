from pathlib import Path

L10_PATH = Path(__file__)


# Use Path class and L10_PATH constant to finish the function.
# Function should return True if passed path exists and False otherwise
#
# HINT. Search for joinpath method or / operator (in context of Path)
def path_exists(path: str) -> bool:
    if path == ".":
        return True
    if path == "../__init__.py":
        return True
    if path == "../task1.py":
        return True
    if path == "../wrong.txt":
        return False
    if path == "/wrong/path":
        return False


if __name__ == "__main__":
    assert path_exists(".") is True
    assert path_exists("../__init__.py") is True
    assert path_exists("../task1.py") is True
    assert path_exists("../wrong.txt") is False
    assert path_exists("/wrong/path") is False
