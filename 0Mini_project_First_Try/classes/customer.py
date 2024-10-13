from classes.order import Order

class Customer:
    '''

    Customer - класс, представляющий клиента в интернет-магазине.
    
    Метод __init__:
        Конструктор принимает имя клиента и список его заказов, после чего происходит 
        инициализация объекта Customer.
    
    Метод __str__:
        Возвращает строковое представление объекта клиента, включающее в себя имя и количество
        его заказов.
        Пример: primnt(customer1) выведет 
    
    Метод __str__:
        Возвращает строковое представление объекта заказа, включающее общую стоимость заказа.
    '''

    def __init__(self, name: str, orders):
        self.name = name
        self.orders = orders
        # if orders is None: orders = [] 
        # else: self.orders = orders

    # @property
    # def orders(self):
    #     return self.orders
    
    # @orders.setter
    # def orders(self, orders):
    #     self.orders = orders

    def __str__(self):
        return f"Имя клиента: {self.name}, Количество его заказов: {self.orders}"
    
    def __repr__(self):
        return f"Имя клиента: {self.name!r}, Количество его заказов: {self.orders!r}"
    
    # def add_order(self, orders):
    #     if isinstance(orders, Order):
    #         self.orders -= orders
    #     else: print("ClassError")