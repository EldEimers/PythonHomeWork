print("Введите баллы: ", end="")
points = int(input())

if points >= 90:
    print("Отлично")
elif points >= 70:
    print("Хорошо")
elif points >= 50:
    print("Сойдёт")
else:
    print("...")