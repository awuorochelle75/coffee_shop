class Coffee:
    def __init__(self,name):
        self.name=name
        self._orders = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) => 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters")
        

    def add_order(self,order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})