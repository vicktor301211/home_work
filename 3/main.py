from tank import Tank
from tkinter import*
KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68
KEY_F = 70

def check_collision():
    if player.intersects(enemy):
        print('Столкновение танков')
def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    if event.keycode == KEY_F:
        player.__fuel = 100
    check_collision()
w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width=800, height=600, bg = 'alice blue')
canv.pack()
player = Tank(canvas=canv, x=100, y=50, ammo=100)
enemy = Tank(canvas=canv, x=300, y=300, ammo=100)
w.bind('<KeyPress>', key_press)
w.mainloop()