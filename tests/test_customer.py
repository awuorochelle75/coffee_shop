import pytest
from customer import Customer
from coffee import Coffee

def test_create_valid_customer():
    c = Customer("Nia")
    assert c.name == "Nia"

def test_invalid_customer_name_type():
    with pytest.raises(ValueError):
        Customer(123)

def test_invalid_customer_name_length():
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLong")

def test_customer_create_order():
    c = Customer("Liam")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 4.0)
    assert order.coffee == coffee
    assert order.customer == c
    assert order in c.orders()
