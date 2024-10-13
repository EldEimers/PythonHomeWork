class Customer:
    
    def __init__(self, name):
        self.name = name
        self.orders = []
        
    def add_to_orders(self, *args):
        for item in args:
            self.orders.append(item)
        # self.orders.append(product)
        
    def remove_from_orders(self, *args):
        for item in args:
            if item in self.orders:
                self.orders.remove(item)
        # if product in self.orders:
        #     self.orders.remove(product)
            
    def __str__(self):
        return f"Имя клиента: {self.name}; Количество его заказов: {len(self.orders)}"
    
    def __repr__(self):
        return f"Имя клиента: {self.name!r}; Количество его заказов: {self.orders!r}"