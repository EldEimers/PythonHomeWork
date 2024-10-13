from classes.customer import Customer
from classes.order import Order
from classes.product import Product
from classes.discount import Discount

#Создаём клиентов
customer1 = Customer("Михаил")
customer2 = Customer("Егор")

#Создаём продукты
product1 = Product("Professional PC", 4500)
product2 = Product("Game PC", 1500)
product3 = Product("Office PC + Kasperski", 299)

#Создаём скидки
promo_dis = Discount("Промо-скидка", 20)
season_dis = Discount("Сезонная скидка", 10)

#Применение скидок
print(f"До применения скидки:\n{product1}")
Discount.apply_discount(product1, promo_dis) #Вторая переменная отвечает за вид скидки
print(f"После применения скидки:\n{product1}")

print(f"До применения скидки:\n{product2}")
Discount.apply_discount(product2, season_dis) #Вторая переменная отвечает за вид скидки
print(f"После применения скидки:\n{product2}")

#Добавляем товары в корзину клиента
customer1.add_to_orders(product1, product2)
customer2.add_to_orders(product3, product3, product3)
customer2.remove_from_orders(product3, product3)

#Оформляем заказы
order1 = Order(customer1)
order2 = Order(customer2)

#Подсчитываем общее кол-во заказов и прибыль с них
print(f"Всего заказов: {Order.total_orders()}\nПрибыль составит: {Order.total_profit()}")

#Выводим информацию о клиентах, заказах и продуктах при помози dunder методов
print(f"Клиенты:\n{customer1}\n{customer2}\nЗаказы:\n{order1}\n{order2}\nНаши товары:\n{product1}\n{product2}\n{product3}\n")