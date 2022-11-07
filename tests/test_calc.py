import pytest
from app.calc import add,subtract,multiply,BankAccount,insufficientfunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50) 

@pytest.mark.parametrize("num1, num2, expected",[
    (3, 2, 5),
    (4,3, 7),
    (20,10,30)
])
def test_add(num1,num2, expected):
    assert add(num1,num2) == expected


def test_subtract():
    assert subtract(5,1) == 4

def test_multiply():
    assert multiply(2, 5) == 10   


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50 

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 20

def test_deposit(bank_account):
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest(bank_account):
    bank_account.collect_interest() 
    assert round(bank_account.balance,6) == 55



@pytest.mark.parametrize("deposited, withdrew, expected",[
    (300, 200, 100),
    (50,20, 30),
    (2000,500,1500)
])

def test_bank_trasnscation(zero_bank_account,deposited,withdrew,expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_balance(bank_account):
    with pytest.raises(insufficientfunds):
        bank_account.withdraw(200)
