from tank import Tank
from tkinter import*
KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68
KEY_F = 70
# KEY_RIGHT = 39
# KEY_LEFT = 37
# KEY_UP = 38
# KEY_DOWN = 40
FPS = 100
CANS = 15
clicks = 0
def update():
    player.update()
    enemy.update()
    check_collision()
    w.after(1000//FPS, update)
def check_collision():
    player.intersects(enemy)
    enemy.intersects(player)
def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    # if event.keycode == KEY_UP:
    #     enemy.forward()
    # if event.keycode == KEY_DOWN:
    #     enemy.backward()
    # if event.keycode == KEY_LEFT:
    #     enemy.left()
    # if event.keycode == KEY_RIGHT:
    #     enemy.right()
    if event.keycode == KEY_F:
        global CANS, clicks
        CANS-=1
        if CANS>0:
            player.refuel()
            print(CANS, 'канистр')
            if 1<CANS<5:
                print(CANS, 'канистры')
            if CANS == 1:
                print(CANS, 'канистра')
        else:
            clicks += 1
            print('Нет канистр c бензином')
            if clicks >= 10:
                print('ЕСЛИ ТЫ ПРОДОЛЖИШЬ НАЖИМАТЬ НА КЛАВИШУ, ИГРА СЛОМАЕТСЯ!')

    check_collision()
w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width=800, height=600, bg = 'alice blue')
canv.pack()
player = Tank(canvas=canv, x=100, y=50, ammo=100, speed=1, bot=False)
enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=True)
enemy.set_target(player)
w.bind('<KeyPress>', key_press)
update()
w.mainloop()