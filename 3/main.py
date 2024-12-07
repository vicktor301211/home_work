import texture
import world
from tank import Tank
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
stop_toggle = False

FPS = 100
CANS = 15
clicks = 0
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
    player = tanks_collect.get_player()
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_SPACE:
        tanks_collect.spawn_enemy()
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
    elif event.keycode == KEY_F:
        global stop_toggle
        if stop_toggle == False:
            player.stop()
            stop_toggle = True

    # check_collision()
def load_textures():
    texture.load('file_up', '../img/tank_up.png')
    texture.load('file_down', '../img/tank_down.png')
    texture.load('file_left', '../img/tank_left.png')
    texture.load('file_right', '../img/tank_right.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    texture.load(world.BRICK, '../img/brick.png')
    print(texture._frames)
w = Tk()
w.title('Танки на минималках 2.0')
load_textures()
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg = 'forest green')
canv.pack()
world.initialise(canv)
tanks_collect.initialize(canv)
w.bind('<KeyRelease>', key_press)
update()
w.mainloop()