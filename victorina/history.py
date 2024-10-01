from random import choice
student = input('Предсатвьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности от 1 до 3: '))
except:
    level = 1
    print('Установлен первый уровень сложности.')
print(f'Хорошо, {student}. Tебе викторина по истории.')
questions = {1: [('В каком году началась Великая Отечественная война?', '1941'),
                 ('Кто был первым президентом США?', 'Джордж Вашингтон')],
             2: [('Кто был первым императором Римской империи?', 'Октавиан Август'),
                 ('В каком году распался Советский Союз?', '1991')],
             3: [('Когда была подписана Магна Карта?', '1215'),
                 ('Кто был фараоном при строительстве пирамид?', 'Хеопс')]}

points = 0
for i in range(3):
    question, correct_answer = choice(questions[level])
    print(f'{student}, {question} ', end='')
    student_answer = input().strip().lower()
    if student_answer == correct_answer.lower():
        points+=1
        print(f'Правильно')
    else:
        print(f'Не правильно, правильный ответ {correct_answer}')
if points == 3:
    print(f'Ах, ну какой умница, {student}. Ты историк!!!')
elif points == 2:
    print(f'Не плохо, {student}. Но ты можешь лучше.')
else:
    print(f'История не твоя сторона, {student}, садись!')