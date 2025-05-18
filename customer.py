#from order import Order

class Customer:
    _all_customers = []
 
    def __init__(self, name):
        self.name = name
        self._orders = []

        Customer._all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)


    @classmethod
    def most_aficionado(cls, coffee):
        top_customer = None
        max_spent = 0.0

        for customer in cls._all_customers:
            total_spent = sum(
                order.price for order in customer.orders() if order.coffee == coffee
            )
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer
        
        return top_customer if max_spent > 0 else None