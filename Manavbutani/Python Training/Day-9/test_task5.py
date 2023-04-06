"""

Modify the first exercise to print a message before and after the execution of each individual test.

"""

from task1 import *
import pytest

@pytest.fixture(autouse=True)
def print_before_after():
    print("Just started\n")
    yield
    print("\nJust ended")
   
@pytest.mark.parametrize("input1,input2,output",[(5,6,11),(6,7,13),(7,7,14)])
def test_task5(input1,input2,output):
    assert sum(input1,input2) == output
    
#pytest -k task5 -vs