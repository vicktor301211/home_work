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


a = ['Камень', 'Ножинцы', 'Бумага']
b = int(input('Сколько раундов хотите играть? '))
for i in range(b):
    c = random.choice(a)
    d = input('Выберите: Камень, Ножницы или Бумагу: ')
    if d == 'Камень' and c == 'Камень':
        print(c)
        print('Ничья')
    elif d == 'Ножницы' and c == 'Ножницы':
        print(c)
        print('Ничья')
    elif d == 'Бумага' and c == 'Бумага':
        print(c)
        print('Ничья')
    elif d == 'Камень' and c == 'Ножницы':
        print(c)
        print('Вы выиграли')
    elif d == 'Ножницы' and c == 'Бумага':
        print(c)
        print('Вы выиграли')
    elif d == 'Бумага' and c == 'Камень':
        print(c)
        print('Вы выиграли')
    elif d == 'Бумага' and c == 'Ножницы':
        print(c)
        print('Вы проиграли')
    elif d == 'Ножницы' and c == 'Камень':
        print(c)
        print('Вы проиграли')
    elif d == 'Камень' and c == 'Бумага':
        print(c)
        print('Вы проиграли')

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