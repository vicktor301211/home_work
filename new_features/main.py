#Импорт библиотек
import missle_collection
from tkinter import*
import world
import tanks_collection
import texture

#Начало игры

start = input('Хотите начать игру? ')
if start == 'да' or start == 'Да':
    print('Тогда в бой!')
else:
    exit("Тогда подготовьтесь и снова начните игру, когда будете готовы")

#Область констант

KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40
KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68
KEY_SPACE = 32
KEY_SHOOT = 13
FPS = 100

#Функция обновления(НИ В КОЕМ СЛУЧАЕ НЕ МЕНЯТЬ!)

def update():
    tanks_collection.update()
    missle_collection.update()
    player = tanks_collection.get_player()
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2 + player.get_size()//2,
                        player.get_y()-world.SCREEN_HEIGHT//2 + player.get_size()//2)
    world.update_map()
    w.after(1000//FPS, update)

#Управление

def key_press(event):
    global tanks_created, level_input, tanks_max
    player = tanks_collection.get_player()
    if player.is_destroyed():
        return
    if event.keycode == KEY_W:
        player.forvard()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(0, -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0, 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5, 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5, 0)

    elif event.keycode == KEY_SHOOT:
        player.fire()

    # elif event.keycode == 32:
    #     tanks_collection.spawn_enemy()


#Функция загрузки текстур

def load_textures():
    texture.load ('tank_down', '../img/tank_down.png')
    texture.load('tank_up', '../img/tank_up.png')
    texture.load('tank_left', '../img/tank_left.png')
    texture.load('tank_right', '../img/tank_right.png')

    texture.load ('tank_down_player', '../img/tank_down_player.png')
    texture.load('tank_up_player', '../img/tank_up_player.png')
    texture.load('tank_left_player', '../img/tank_left_player.png')
    texture.load('tank_right_player', '../img/tank_right_player.png')
    texture.load('tank_destroyed', '../img/tank_destroy.png')

    texture.load('full_hp', '../img/100.png')
    texture.load('75', '../img/75.png')
    texture.load('50', '../img/50.png')
    texture.load('25', '../img/25.png')
    texture.load('0', '../img/0.png')


    texture.load(world.BRICK,'../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    texture.load(world.MISSLE, '../img/bonus.png')

    texture.load('missile_up', '../img/missile_up.png')
    texture.load('missile_down', '../img/missile_down.png')
    texture.load('missile_left', '../img/missile_left.png')
    texture.load('missile_right', '../img/missile_right.png')
#Создание окна
w = Tk()
load_textures()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg = 'forest green')
canv.pack()
#Инициализация файлов кода, так же проверка нажатий на клавиши
world.initialize(canv)
tanks_collection.initialize(canv)
missle_collection.initialise(canv)
w.bind('<KeyRelease>', key_press)
update()
#Зацикливание окна
w.mainloop()
