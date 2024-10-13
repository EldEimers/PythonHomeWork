# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount



# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)

# Рассчитываем цену с учетом скидки
discounted_price = Order.calculate_discounted_price(product1.price, 10)
print(f"Сниженная цена на {product1.name}: {discounted_price}")  # Вывод: Сниженная цена на Laptop: 900.0

# Создаем заказы
order1 = Order([product1])
order2 = Order([product2, product1])

# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")  # Вывод: Всего заказов: 2

# Выводим информацию о заказах
print(order1)  # Вывод: Заказ (Общая цена = 1000)
print(order2)  # Вывод: Заказ (Общая цена = 1500)


print("\n-\n-\n-\nМои проверки:\n")

"""
Создание продуктов:

    product1 создается с названием "Laptop" и ценой 1000.
    product2 создается с названием "Smartphone" и ценой 500.

Расчет цены с учетом скидки:

    Рассчитывается цена product1 с 10% скидкой. Результат: 900.0.
    print(f"Discounted price of {product1.name}: {discounted_price}") выводит: Discounted price of Laptop: 900.0.

Создание заказов:

    order1 создается с одним товаром product1.
    order2 создается с двумя товарами: product1 и product2.

Общее количество заказов:

    Order.total_orders() возвращает 2, так как были созданы два заказа.
    print(f"Total orders: {Order.total_orders()}") выводит: Total orders: 2.

Информация о заказах:

    print(order1) выводит: Order(total_price=1000), так как в order1 только один товар product1 с ценой 1000.
    print(order2) выводит: Order(total_price=1500), так как в order2 два товара: product1 и product2 с общей ценой 1500.
"""


'''
Мои проверки
'''

season_discount = Discount("Сезонная скидка", 15)
promo_discount = Discount("Скидка по промокоду", 20)

product3 = Product("Python course", 777)
product4 = Product("PC", 600)

product4.price = Discount.calc_discount_price(product4.price, promo_discount.discount_percent)

order3 = Order([product4])
order4 = Order([product4, product3])

customer1 = Customer("Михаил", order3)
customer2 = Customer("Вася", order4)

print(customer1)
print(customer2)

print(order3)
print(order4)

print(product3)
print(product4)

print(f"Всего заказов: {Order.total_orders()}")
print(f"Общий доход со всех заказов: {Order.total_profit()}")

print("\/ Проверка на \"равно\" \/")

product5 = Product("Носки Add", 50)
product6 = Product("Носки Pum", 50)
product7 = Product("Носки Gach", 500)

print(product5 == product6)
print(product6 == product7)

print("\/ Проверка на \"меньше чем\" \/")

print(product5 < product6)
print(product6 < product7)\

print(customer1)
print(repr(customer1))