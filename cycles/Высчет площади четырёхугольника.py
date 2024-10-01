a = input('Хотите работать с программой? ')
while a != 'нет':
    b = int(input('Длина: '))
    c = int(input('Ширина: '))
    formula = b*c
    print(formula)
    a = input('Хотите продолжить работать с программой? ')
print('Сеанс работы завершён')