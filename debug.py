from customer import Customer
from coffee import Coffee
from order import Order

def run_tests():
    print("=== Test Customer Creation ===")
    try:
        c = Customer("Nia")
        print("Customer created:", c.name)
    except Exception as e:
        print("Customer creation failed:", e)

    print("\n=== Test Coffee Creation ===")
    try:
        coffee = Coffee("Latte")
        print("Coffee created:", coffee.name)
    except Exception as e:
        print("Coffee creation failed:", e)

    print("\n=== Test Order Creation ===")
    try:
        order = Order(c, coffee, 4.5)
        print(f"Order created: {order.customer.name} ordered {order.coffee.name} for ${order.price}")
    except Exception as e:
        print("Order creation failed:", e)

    print("\n=== Test Invalid Customer Name ===")
    try:
        Customer(123)
    except Exception as e:
        print("Expected error:", e)

    print("\n=== Test Invalid Coffee Name ===")
    try:
        Coffee("A")
    except Exception as e:
        print("Expected error:", e)

    print("\n=== Test Invalid Order Price ===")
    try:
        Order(c, coffee, 20)
    except Exception as e:
        print("Expected error:", e)

if __name__ == "__main__":
    run_tests()
