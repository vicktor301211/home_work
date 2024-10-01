from random import choice
student = input('Предсатвьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности от 1 до 3: '))
except:
    level = 1
    print('Установлен первый уровень сложности.')
print(f'Хорошо, {student}. Tебе викторина по географии.')
questions = {1: [('Столица России?', 'Москва'), ('Столица Франции?', 'Париж'),
                 ('Столица Италии?', 'Рим')],
             2: [('Самая большая страна по площади?', 'Россия'), ('На каком материке находится Австралия?', 'Австралия'),
                 ('Самая длинная река?', 'Амазонка')],
             3: [('Какое море самое солёное?', 'Мёртвое море'), ('Самая густонаселённая страна?', 'Китай'),
                 ('Столица Италии?', 'Рим')]}

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
    print(f'Ах, ну какой умница, {student}. Ты знаток географии!!!')
elif points == 2:
    print(f'Не плохо, {student}. Но ты можешь лучше.')
else:
    print(f'География не твоя сторона, {student}, садись!')