access = False
correct_password = "Rick"

print("Введите пароль: ")

user_answer = input()
print()

while(not access):
    if user_answer != correct_password:
        print("Пароль неверен..\n")
        print("Введите пароль: ")
        user_answer = input()
    else:
        access = not access
        print("\nДобро пожаловать!\n")

