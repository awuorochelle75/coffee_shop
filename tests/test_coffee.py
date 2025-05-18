import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_create_valid_coffee():
    c = Coffee("Espresso")
    assert c.name == "Espresso"

def test_invalid_coffee_name():
    with pytest.raises(ValueError):
        Coffee("A")

def test_add_order_and_customers():
    coffee = Coffee("Latte")
    customer = Customer("Zoe")
    order = Order(customer, coffee, 3.5)
    assert order in coffee.orders()
    assert customer in coffee.customers()
    assert coffee.num_orders() == 1
    assert coffee.average_price() == 3.5
