from random import choice

HangMan = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

tries = len(HangMan) - 1
Words = ("Never", "Rick", "Gonna", "Roll")
word = choice(Words)

progress = "_" * len(word)
mistakes = 0
used = []

while mistakes < tries and progress != word:
    print(HangMan[mistakes])
    print("Были использованы следующие буквы:\n", used)
    print("\nЗагаданное слово выглядит так:\n", progress)
    
    guess = input("\n\nВведите букву: ")
    
    while guess in used:
        print("Вы уже вводили эту букву", guess)
        guess = input("Введите новую букву: ")
        
    used.append(guess)
    
    if guess in word:
        print("\n Верно!", guess, "есть в слове.")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += progress[i]
        progress = new
    else:
        print("\nК сожалению, буквы \"" + guess + "\" нет в слове..")
        mistakes += 1

if mistakes == tries:
    print(HangMan[mistakes])
    print("\nДопрыгался!")
    print("Загаданное слово было: \"" + word + "\"...")
else:
    print("\nВы угадали слово \"" + word + "\"!")