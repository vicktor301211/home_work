from random import *
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

from random import choice
student = input('Предсатвьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности от 1 до 3: '))
except:
    level = 1
    print('Установлен первый уровень сложности.')
print(f'Хорошо, {student}. Tебе викторина на знание животных.')
animals = {1: [('Серое животное с хоботом?', 'Слон'), ('Коричневый мохнатый зверь, который любит мёд?', 'Медведь')],
             2: [('Хищник - король джунглей семейства кошачьих?', 'Лев'), ('Животное, живущее в антарктиде и умеющее плавать?', 'Пингвин')],
             3: [('Млекопитающее, являющееся самым больным животным из всех?', 'Синий кит'), ('ночной хищник, который имеет возможность выживать без воды в пустыне и относится к псовым?', 'Фенек')]}

points = 0
for i in range(3):
    question, correct_answer = choice(animals[level])
    print(f'{student}, что это за животное: {question} ', end='')
    student_answer = input().strip().lower()
    if student_answer == correct_answer.lower():
        points+=1
        print(f'Правильно')
    else:
        print(f'Не правильно, правильный ответ {correct_answer}')
if points == 3:
    print(f'Ах, ну какой умница, {student}. Ты знаток животных!!!')
elif points == 2:
    print(f'Не плохо, {student}. Но ты можешь лучше.')
else:
    print(f'Ты плохо знаешь животных, {student}, садись!')

student = input('Предсатвьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности от 1 до 5: '))
except:
    level = 1
    print('Установлен первый уровень сложности.')
animals_easy = ['кот', 'пёс', 'корова', 'лошадь', 'курица']
animals_hard = ['жираф', 'кенгуру', 'носорог', 'панда', 'лягушка']
if level > 3:
    animals = animals_hard
else:
    animals = animals_easy
points = 0
for i in range(5):
    animal = choice(animals)
    print(
        f'{student}, угадай животное. Длина слова: {len(animal)} букв, '
        f'оно начинается на "{animal[0]}" и заканчивается на "{animal[-1]}"')
    answer = input('Твой ответ: ')
    if answer == animal:
        points+=1
        print(f'Правильно')
    else:
        print(f'Не правильно, правильный ответ {animal}')
if points == 5:
    print(f'Ах, ну какой умница, {student}. Ты знаток животных!!!')
elif points >= 2:
    print(f'Не плохо, {student}. Но ты можешь лучше.  У тебя {points} правильных ответов')
else:
    print(f'Ты плохо знаешь животных, {student}, садись! У тебя {points} ответов')