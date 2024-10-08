print("Введите баллы: ", end="")
points = int(input())

match points:
    case points if points >= 90:
        print("Отлично")
    case points if points >= 70:
        print("Хорошо")
    case points if points >= 50:
        print("Сойдёт")
    case _:
        print("...")