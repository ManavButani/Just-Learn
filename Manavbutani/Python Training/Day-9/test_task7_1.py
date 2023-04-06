"""
Write unit tests for the function created for Day-4 Hands-on with at least 2-3 different scenarios for each
question.
Question no. - 6, 7, 8 & 9.

"""
import pytest


class MyError(Exception):
    pass

def check(j):
    try:
        j = int(j)
    except ValueError as e:
        raise MyError("Entered value can't be converted to integer!!")
    else:
        return 1

@pytest.mark.parametrize("num, output", [(1, 1), (7, 1), (5, 1)])
def test_task7_1_0(num, output):
    assert check(num) == output

def test_task7_1_1():
    with pytest.raises(MyError):
        assert check("test")