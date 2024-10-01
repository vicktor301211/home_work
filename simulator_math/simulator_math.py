from random import randint
student = input('Предсатвьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности от 1 до 5: '))
except:
    level = 1
    print('Установлен первый уровень сложности.')
if level <1 or level>5:
    level = 1
    print('Установлен первый уровень сложности.')
print(f'Хорошо, {student}. Tебе задача.')
minimum =  10**(level - 1)
maximum =  10**level - 1
points = 0
for i in range(5):
    a = randint(minimum, maximum)
    b = randint(minimum, maximum)
    print(f'{student}, сколько будет {a}+{b}? ', end='')
    correct_answer = a+b
    student_answer = input()
    if student_answer == str(correct_answer):
        points+=1
        print(f'Правильно')
    else:
        print(f'Не правильно, правильный ответ {correct_answer}')
if points == 5:
    print(f'Ах, ну какой умница, {student}. Это пять!!!')
elif points == 4:
    print(f'Не плохо, {student}. Но ты можешь лучше. Садись, пожалуйста, четыре.')
elif points == 3:
    print(f'Так себе, {student}. Садись, тройка.')
else:
    print(f'Два, {student}, садись!')