"""
Write a method which returns the nth fibonacci number. Write a single, parameterized unit test to test the
method.

"""
import pytest

@pytest.mark.parametrize("num, output", [(1, 1), (7, 13), (5, 5), (6, 8)])
def test_fibo(num, output):
    assert fibbo(num) == output

def fibbo(n):
    i = 0
    x = [0, 1]
    z = 0

    if n in [0, 1]:
        z = n
        # print(f"Your {n}th fibonacci element is {z}")
        return z

    else:
        while i < int(n) - 1:
            z = x[len(x) - 2] + x[len(x) - 1]
            x.append(z)
            i += 1
        # print(f"Your {n}th fibonacci element is {z}")
        return z