import random

print("Добро пожаловать в игру Угадай число!")

while True:
    print("\nВыбери уровень сложности:")
    print("1. Лёгкий (от 1 до 10, попыток: 3)")
    print("2. Средний (от 1 до 100, попыток: 7)")
    print("3. Сложный (от 1 до 1000, попыток: 10)")
    
    choice = input("Твой выбор (1, 2 или 3): ")
    
    if choice == "1":
        max_num = 10
        max_attempts = 3
    elif choice == "3":
        max_num = 1000
        max_attempts = 10
    else:
        max_num = 100
        max_attempts = 7

    secret = random.randint(1, max_num)
    attempts = 0
    
    print(f"\nЯ загадал число от 1 до {max_num}. У тебя есть {max_attempts} попыток!")

    while attempts < max_attempts:
        guess = int(input("Твой вариант: "))
        attempts += 1
        
        if guess < secret:
            print(f"Больше! Осталось попыток: {max_attempts - attempts}")
        elif guess > secret:
            print(f"Меньше! Осталось попыток: {max_attempts - attempts}")
        else:
            print(f"Поздравляю! Ты угадал число {secret} за {attempts} поп.")
            break
    else:
        print(f"Ты проиграл! Загаданное число было: {secret}")

    again = input("\nСыграть ещё раз? (да/нет): ")
    if again.lower() != "да":
        print("Спасибо за игру!")
        break