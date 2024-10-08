access = False

user_password = "Roll"

print("Введите пароль: ", end="")
user_answer = input()

while(not access):    
    if user_answer != user_password:
        code = 2
    elif user_answer == user_password:
        code = 1
    else:
        code = 3
    match code:
        case 1:
            print("\nДобро пожаловать!\n")
            access = not access
        case 2:
            print("Пароль неверен...")
            print("Введите пароль заново: ", end="")
            user_answer = input()
        case _:
            print("WTH")