class Order:

    _total_orders = 0
    _total_profit = 0
    
    def __init__(self, customer):
        self.customer = customer
        self.products = customer.orders
        Order._total_orders += 1
        Order._total_profit += sum(item.price for item in self.products)
        
    @classmethod
    def total_orders(cls):
        return cls._total_orders
    
    @classmethod
    def total_profit(cls):
        return cls._total_profit
    
    def total_price(self):
        return sum(product.price for product in self.products)
    
    def __str__(self) -> str:
        return f"Заказ (Общая цена = {self.total_price()})"
    
    def __repr__(self):
        return f"Заказ (Общая цена = {self.total_price()!r})"