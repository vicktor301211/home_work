import world
from tank import Tank
from tkinter import*
KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68
KEY_F = 70
KEY_RIGHT = 39
KEY_LEFT = 37
KEY_UP = 38
KEY_DOWN = 40

FPS = 100
CANS = 15
clicks = 0
def update():
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH//2+player.get_size()//2,
                        player.get_y() - world.SCREEN_HEIGHT//2+player.get_size()//2)
    player.update()
    enemy.update()
    neutral.update()
    check_collision()
    w.after(1000//FPS, update)
def check_collision():
    player.intersects(enemy)
    enemy.intersects(player)
def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
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
    check_collision()
w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width=world.SCREEN_WIDTH, height=world.SCREEN_HEIGHT, bg = 'alice blue')
canv.pack()
player = Tank(canvas=canv, x=100, y=50, ammo=100, speed=1, bot=False)
enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=True)
neutral = Tank(canvas=canv, x=200, y=200, ammo=100, speed=1, bot=False)
neutral.stop()
enemy.set_target(player)
w.bind('<KeyPress>', key_press)
update()
w.mainloop()