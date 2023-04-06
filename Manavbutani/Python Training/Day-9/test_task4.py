"""
Modify the tests from the second exercise so that only one instance of Account is used across all tests
using fixtures.

"""

import pytest
from test_task2 import Account,UnSufficiantBalanceError

@pytest.fixture
def object_container():
    return Account(50000)
    
def test_add_task4(object_container):
    assert object_container.add(500) == 50500
    
def test_sub_task4(object_container):
    with pytest.raises(UnSufficiantBalanceError):
        assert object_container.sub(50000)
    