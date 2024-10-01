import random
a = ['Камень', 'Ножинцы', 'Бумага']
b = int(input('Сколько раундов хотите играть? '))
c = random.choice(a)
for i in range(b):
    d = input('Выберите: Камень, Ножницы или Бумагу: ')
    if d == 'Камень' and c == 'Камень':
        print(c)
        print('Ничья')
    if d == 'Ножницы' and c == 'Ножницы':
        print(c)
        print('Ничья')
    if d == 'Бумага' and c == 'Бумага':
        print(c)
        print('Ничья')
    if d == 'Камень' and c == 'Ножницы':
        print(c)
        print('Вы выиграли')
    if d == 'Ножницы' and c == 'Бумага':
        print(c)
        print('Вы выиграли')
    if d == 'Бумага' and c == 'Камень':
        print(c)
        print('Вы выиграли')
    if d == 'Бумага' and c == 'Ножницы':
        print(c)
        print('Вы проиграли')
    if d == 'Ножницы' and c == 'Камень':
        print(c)
        print('Вы проиграли')
    if d == 'Камень' and c == 'Бумага':
        print(c)
        print('Вы проиграли')