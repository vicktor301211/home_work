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