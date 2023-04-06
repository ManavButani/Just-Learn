"""
Create a class `Account` with an int attribute `balance` and two methods add, and subtract which only take
a single positive integer as an argument and respectively adds or subtracts them from the balance or
raises ValueError if the balance is not sufficient. Write unit tests to test all the methods with 100%
coverage.

"""
import pytest

class UnSufficiantBalanceError(Exception):
    pass


class Account:
    
    def __init__(self,balance) -> None:
        self.balance=balance
        
    # @pytest.fixture(name="test_value")
    def add(self,val):
        self.balance =self.balance + val
        return self.balance
    
    def sub(self,val):
        self.balance =self.balance - val
        if self.balance < 1000:
            self.balance =self.balance + val
            raise UnSufficiantBalanceError("Not Enough Balance")
        return self.balance

    
@pytest.mark.test_value
def test1():
    a1=Account(50000)
    assert a1.add(5) == 50005
    
@pytest.mark.test_value
def test2():
    a1=Account(50000)
    with pytest.raises(UnSufficiantBalanceError):
        assert a1.sub(50000)