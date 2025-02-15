from tkinter import NW
from random import randint
from missle_collection import check_missiles_collision
from units import Tank
import world
name = input('Введите вашу фамилию: ')
operation = input('Введите название операции: ')

print(f''' - Здравия желаю, товарищ лейтенант! Сегодня майор Жуков проведёт вам инструктаж. Проследуйте пожалуйста за мной.
Вы молча следуете за сержантом Бобриковым в кабинет майора Жукова.
 - Здравия желаю, товарищ майор! - говорите вы, - Лейтенант {name} прибыл для прохождения инструктажа!
 - Присаживайся, лейтенант. Итак, как ты уже знаешь, на завтра намечена операция "{operation}". Ты назначаешься
командиром танковой группы номер 3. Линия фронта большая, так что не надейcя на поддержку подчинённых.
Управлять танком ты умеешь, но я напомню: WASD - смена направления. Стрелять на Enter. Там могут быть
раскиданы снаряды, их можешь подобрать. Снаряды разрушат кирпич, так что если совсем уже некуда, то через
кирпичи. На воде ехать будешь медленнее, нежели по земле. Бетон разрушить не получится. Ну, ни пуха, ни пера!
Вы уходите от майора Жукова и приказываете команде готовиться к операции''')

_tanks = []
_canvas = None
id_screen_text = 0

def initialize(canv):
    global _canvas, id_screen_text, hp_id
    _canvas = canv
    # spawn(False)
    # for i in range(1):
    #     spawn(True).set_target(get_player())
    player = spawn(False)
    enemy = spawn(True).set_target(player)
    spawn(True).set_target(player)
    id_screen_text = _canvas.create_text(10, 10, text = _get_screen_text(), font = ('TkDefaultFont', 20), fill = 'white', anchor = NW)
    hp_id = _canvas.create_text(600, 10, text = _get_hp_text(), font = ('TkDefaultFont', 20), fill = 'white', anchor = NW)
def exit_on_death():
    exit(f'''               Отчёт об операции "{operation}":
Операция была провалена. Танковая группа 3 была уничтожена. 
В общей сумме было потеряно 6 танков, среди которых танк лейтенанта {name}.
Также потери: Танк сержанта Сидорова, БМП прапорщика Кемерова, два военных вертолёта, 
50 человек пехоты, танк старшины Петрова, также три танка, командиров которых опознать не удалось.
Лейтенант {name} удостоен звания Герой России(посмертно).
Отчёт составил: главнокомандующий силами операции "{operation}":
Майор Иван Жуков''')
def exit_on_win():
    exit(f'''               Отчёт об операции "{operation}":
Операция проведена успешно. Танковая группа 3 отбила высоту Альфа у противника. 
В общей сумме был потерян 1 танк прапорщика Валентира(загорелся ещё до начала операции).
Лейтенант {name} удостоен звания Герой России.
Отчёт составил: главнокомандующий силами операции "{operation}":
Майор Иван Жуков''')
def _get_screen_text():
    global _canvas, id_screen_text
    if get_player().is_destroyed():
        exit_on_death()
        return 'Ваш танк уничтожен'
    if len(_tanks) == 1:
        exit_on_win()
        return 'Высота отбита у врага'
    return 'Осталось {}'.format(len(_tanks)-1)
def _get_hp_text():
    global _canvas, hp_id
    if get_player().is_destroyed():
        return 'Здоровье: 0'
    return 'Здоровье: {}'.format(get_player()._hp)
def update_screen_text():
    _canvas.itemconfig(id_screen_text, text = _get_screen_text())
    _canvas.itemconfig(hp_id, text = _get_hp_text())

def get_player():
    return _tanks[0]

def update():
    global _canvas
    update_screen_text()
    start = len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i != 0:
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
            check_missiles_collision(_tanks[i])

def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
    return False



def spawn(is_bot=True):
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols-1)
        row = randint(1, rows-1)

        if world.get_block(row, col) != world.GROUND:
            continue

        t = Tank(_canvas, row,col, bot=is_bot)
        if not check_collision(t):
            _tanks.append(t)
            return t