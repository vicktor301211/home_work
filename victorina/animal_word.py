from random import choice
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