import random
a = input('Хотите работать с программой? ')
while a != 'нет':
    b = int(input('Длина: '))
    c = int(input('Ширина: '))
    formula = b*c
    print(formula)
    a = input('Хотите продолжить работать с программой? ')
print('Сеанс работы завершён')


a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
b = []
d = int(input('Сколько знаков хотите? '))
for i in range(d):
    c = random.choice(a)
    print(c)

print('Правила игры: ')
print('Камень ломает ножницы, ножницы стригут бумагу, бумага оборачивает камень')
user_action = input("Сделайте выбор — камень, ножницы, бумага или выход (пишите с маленькой буквы): ")
possible_actions = ["камень", "бумага", "ножницы"]
computer_action = random.choice(possible_actions)
while user_action!='выход':
    print('Вы выбрали', user_action, ' компьютер выбрал', computer_action)
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action}. Ничья!!")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == "ножницы":
        if computer_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
    else:
        print('Ошибка')
    user_action = input("Сделайте выбор — камень, ножницы, бумага или выход: ")
    computer_action = random.choice(possible_actions)
print('До встречи!!!')



a = int(input('Число: '))
for i in range(1):
    print('Квадрат: ', a*a)
    print('Куб: ', a*a*a)


anwsers = ['Точно нет', 'сложно сказать', 'шансы малы', 'не могу сказать', 'Возможно', 'вероятнее да', 'шансы высоки', 'точно да']
print('Здравствуй, странник.')
n = input('Хочешь ответ??? ')
while n!='нет':
    print('Задай вопрос.')
    input()
    print(random.choice(anwsers))
    n = input('Хочешь ответ??? ')
print('До встречи!!!')

a = input('Хотите смешивать цвета?: ')
while a == 'да':
    d = input('1 цвет: ')
    c = input('2 цвет: ')
    if d == 'Красный' and c == 'Синий':
        print('Фиолетовый')
    elif d == 'Красный' and c == 'Зелёный':
        print('Жёлтый')
    elif d == 'Зелёный' and c == 'Красный':
        print('Жёлтый')
    elif d == 'Зелёный' and c == 'Синий':
        print('Цвет морской волны')
    elif d == 'Синий' and c == 'Красный':
        print('Фиолетовый')
    elif d == 'Синий' and c == 'Зелёный':
        print('Цвет морской волны')
    else:
        print('программна не смешивает такие цвета. Смешиваются красный, зелёный и синий. Цвета пишутся с большой буквы')
    a = input('Хотите смешивать цвета?: ')