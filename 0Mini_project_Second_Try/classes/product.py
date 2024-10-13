class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self) -> str:
        return f"Продукт {self.name} имеет стоимость в {self.price} долларов."
    
    def __repr__(self) -> str:
        return f"Продукт {self.name!r} имеет стоимость в {self.price!r} долларов."
    
    def __eq__(self, other: object):
        return self.price == other.price
    
    def __lt__(self, other: object):
        return self.price < other.price