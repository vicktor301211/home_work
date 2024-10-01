import random
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
b = []
d = int(input('Сколько знаков хотите? '))
for i in range(d):
    c = random.choice(a)
    print(c)
