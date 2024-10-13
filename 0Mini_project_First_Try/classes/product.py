class Product:
    """
    Класс Product

    Этот класс представляет товар в интернет-магазине.

    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
        Пример: product1 = Product("Laptop", 1000) создаст товар с названием "Laptop" и ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(product1) выведет Product(name=Laptop, price=1000).
    """
    def __init__(self, name: str, price: float | int):
        self.name = name
        self.price = price

    # @property
    # def price(self):
    #     return self.price
    
    # @price.setter
    # def price(self, price: float | int):
    #     if price >= 0: self.price = price

    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={round(self.price)})"
    
    def __repr__(self):
        return f"Продукт (Название={self.name!r}, Цена={round(self.price)!r})"
    
    def __eq__(self, other: object):
        return self.price == other.price
    
    def __lt__(self, other: object):
        return self.price < other.price