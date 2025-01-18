import texture
import world
#from tank import Tank
from tkinter import*
import tanks_collect


KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68
KEY_F = 70
KEY_RIGHT = 39
KEY_LEFT = 37
KEY_UP = 38
KEY_DOWN = 40
KEY_SPACE = 32
KEY_ESC = 27
stop_toggle = False

FPS = 100
CANS = 15
tanks_created = 0
tanks_max = 10
# level_input = int(input('Введите уровень сложности: '))
# if level_input < 1 or level_input > 3:
#     if level_input > 3 and level_input != 100:
#         print('Дружище, ты не справишься. Давай лучше на третьем поиграй')
#         level_input = 3
#     if level_input < 1:
#         level_input = 100
#         print('Читерить нельзя! РКН вас наказал!')
def update():
    tanks_collect.update()
    player = tanks_collect.get_player()
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH//2+player.get_size()//2,
                        player.get_y() - world.SCREEN_HEIGHT//2+player.get_size()//2)
    # player.update()
    # enemy.update() - не используется
    # neutral.update()
    # check_collision()
    world.update_map()
    w.after(1000//FPS, update)
# def check_collision():
#     player.intersects(enemy)
#     enemy.intersects(player)
def key_press(event):
    global tanks_created, tanks_max
    player = tanks_collect.get_player()
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    # elif event.keycode == KEY_SPACE:
    #     tanks_collect.spawn(True)
    #     tanks_created += 1
    #     print(tanks_created)
    #     if level_input == 1:
    #         tanks_max = 20
    #     elif level_input == 2:
    #         tanks_max = 25
    #     elif level_input == 3:
    #         tanks_max = 30
    #     elif level_input == 100:
    #         for i in range(100000000000000000000000000000000000000)^
    #           print('!')
    #     if tanks_created >= tanks_max:
    #         exit('MemoryAccessViolation in /../3/main/(exit code: -2784221268) (Ошибка выделения памяти(код ошибки: -2784221268))')

    elif event.keycode == KEY_ESC:
        exit('Выход из игры')
    # elif event.keycode == KEY_UP:
    #     world.move_camera(0, -5)
    # elif event.keycode == KEY_DOWN:
    #     world.move_camera(0, 5)
    # elif event.keycode == KEY_LEFT:
    #     world.move_camera(-5, 0)
    # elif event.keycode == KEY_RIGHT:
    #     world.move_camera(5, 0)
    # elif event.keycode == KEY_F:
    #     global CANS, clicks
    #     CANS-=1
    #     if CANS>0:
    #         player.refuel()
    #         enemy.refuel()
    #         print(CANS, 'канистр')
    #     else:
    #         clicks += 1
    #         print('Нет канистр c бензином')
    #         if clicks >= 10:
    #             print('ЕСЛИ ТЫ ПРОДОЛЖИШЬ НАЖИМАТЬ НА КЛАВИШУ, ИГРА СЛОМАЕТСЯ!')
    #         if clicks == 15:
    #             canv.delete(player.id, enemy.id)
    #             canv.create_text(world.WIDTH//2, world.HEIGHT//2, text='ВАМ ЖЕ БЫЛО СКАЗАНО, НЕ ПРОДОЛЖАТЬ НАЖИМАТЬ НА КНОПКУ!', font=('Arial', 15))

    # check_collision()
def load_textures():
    texture.load('file_up', '../img/tank_up.png')
    texture.load('file_down', '../img/tank_down.png')
    texture.load('file_left', '../img/tank_left.png')
    texture.load('file_right', '../img/tank_right.png')
    texture.load('file_up_player', '../img/tank_up_player.png')
    texture.load('file_down_player', '../img/tank_down_player.png')
    texture.load('file_left_player', '../img/tank_left_player.png')
    texture.load('file_right_player', '../img/tank_right_player.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    texture.load(world.BRICK, '../img/brick.png')
    texture.load(world.MISSLE, '../img/bonus.png')
    print(texture._frames)
w = Tk()
w.title('Танки на минималках 2.0')
load_textures()
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg = 'forest green')

canv.pack()
world.initialize(canv)
tanks_collect.initialize(canv)
w.bind('<KeyRelease>', key_press)
update()
w.mainloop()