import pytest
from test_checkout import Checkout

@pytest.fixture()
def checkout():
    checkout=Checkout()
    return checkout

def test_CanAddItemPrice(checkout):
    checkout.addItemPrice("a",1)

def test_CanAddItem(checkout):
    checkout.addItem("b")

def test_CanCalculateTotal(checkout):
    assert checkout.calculateTotal()==0

def test_GetCorrectTotalWithMultipleItem(checkout):
    checkout.addItemPrice("a",1)
    checkout.addItemPrice("b",2)
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal()==3
