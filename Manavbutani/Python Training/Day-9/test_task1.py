from task1 import sum
import pytest
def test_sum():
    assert sum(10,20) == 30
    
def test_sum1():
    with pytest.raises(ValueError, match="Only positive numbers are allowed"):
        assert sum(1, -1555)