class Discount:
    '''
    
    Класс Discount - класс, который отвечает за функционал скидок.
    
    Метод __init__:
        Конструктор инициализирует объект Discount с двумя атрибутами: description (описание скидки) и 
        discount_percent (процент скидки).
    
     Метод __str__:
        Возвращает строковое представление объекта: описание и процент скидки.
        
    '''
    
    def __init__(self, description: str, discount_percent: float | int):
        self.description = description
        self.discount_percent = discount_percent
    
    @staticmethod
    def calc_discount_price(price: float | int, discount):
        return price * (1 - discount / 100)

    
    def __str__(self):
        return f"Описание скидки: {self.description}, Скидка={self.discount_percent}%)"
    
    def __repr__(self):
        return f"Описание скидки: {self.description!r}, Скидка={self.discount_percent!r}%)"