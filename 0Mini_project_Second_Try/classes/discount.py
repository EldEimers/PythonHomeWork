class Discount:
    
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent
        
    
    
    @staticmethod
    def apply_discount(product, discount):
        product.price *= 1 - (discount.discount_percent / 100)
        
    def __str__(self) -> str:
        return f"Описание скидки: {self.description}; Её значение: {self.discount_percent}"
    
    def __repr__(self) -> str:
        return f"Описание скидки: {self.description!r}; Её значение: {self.discount_percent!r}"