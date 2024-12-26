from random import randint
from tank import Tank
import world


_tanks = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv
    # player = Tank(canvas=canv, x=world.BLOCK_SIZE*2, y=world.BLOCK_SIZE*4, ammo=100, speed=2, bot=False)
    # enemy = Tank(canvas=canv, x=world.BLOCK_SIZE*4, y=world.BLOCK_SIZE*6, ammo=100, speed=2, bot=True)
    # # neutral = Tank(canvas=canv, x=200, y=200, ammo=100, speed=1, bot=False)
    # # neutral.stop()
    # enemy.set_target(player)
    # _tanks.append(player)
    # _tanks.append(enemy)
    # # _tanks.append(neutral)
    # print(_tanks)
    spawn(False)
    for i in range(3):
        spawn(True).set_target(get_player())
def get_player():
    return _tanks[0]
# def spawn_enemy():
#     while True:
#         pos_x = randint(200, 800)
#         pos_y = randint(200, 600)
#         t = Tank(canvas=_canvas, x=pos_x, y=pos_y, speed=1)
#         if not check_collision(t):
#             t.set_target(get_player())
#             _tanks.append(t)
#             return True
def spawn(is_bot = True):
    global tanks_count
    cols = world.get_cols()
    rows = world.get_rows()
    while True:
        col = randint(1, cols-1)
        row = randint(1, rows-1)
        if world.get_block(row, col) != world.WATER:
            continue
        t = Tank(_canvas, x = col*world.BLOCK_SIZE, y = row*world.BLOCK_SIZE, speed=2, bot = is_bot)
        if not check_collision(t):
            _tanks.append(t)
            return t
def update():
    for tank in _tanks:
        tank.update()
        check_collision(tank)
def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
    return False