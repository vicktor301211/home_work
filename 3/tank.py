from tkinter import PhotoImage

from hitbox import Hitbox
class Tank:
    __count = 0
    __SIZE = 100
    def __init__(self,canvas,x,y,ammo = 100, model = 'T - 14 Армата',speed = 10, file_up = '../img/tank_up.png', file_down = '../img/tank_down.png',
                 file_left = '../img/tank_left.png', file_right = '../img/tank_right.png'):
        self.__skin_up = PhotoImage(file=file_up)
        self.__skin_down = PhotoImage(file=file_down)
        self.__skin_left = PhotoImage(file=file_left)
        self.__skin_right = PhotoImage(file=file_right)
        self.__hitbox = Hitbox(x, y, Tank.__SIZE, Tank.__SIZE)
        self.__canvas = canvas
        Tank.__count+=1
        self.__model = model #моедль
        self.__fuel = 1000000
        self.__speed = speed
        self.__hp = 100 #здоровье
        self.__xp = 0 #опыт
        self.__ammo = ammo #боекомплект
        self.__x = x#положение по оси х
        self.__y = y #положение по оси у
        if self.__x < 0:
            self.__x=0
        if self.__y < 0:
            self.__y=0
        self.__create()
    def fire(self):
        if self.__ammo > 0:
            self.__ammo-=1
            print('стреляю')
        else:
            print('Нет снарядов')
    def backward(self):
        if self.__fuel>0:
            self.__y+=self.__speed
            self.__update_hitbox()
            self.__repaint()
            self.__fuel-=1
            self.__canvas.itemconfig(self.id, image=self.__skin_down)
            self.__repaint()
    def forward(self):
        if self.__fuel>0:
            self.__y+=-self.__speed
            self.__update_hitbox()
            self.__repaint()
            self.__fuel-=1
            self.__canvas.itemconfig(self.id, image=self.__skin_up)
            self.__repaint()
    def left(self):
        if self.__fuel>0:
            self.__x+=-self.__speed
            self.__update_hitbox()
            self.__repaint()
            self.__fuel-=1
            self.__canvas.itemconfig(self.id, image=self.__skin_left)
            self.__repaint()
    def right(self):
        if self.__fuel>0:
            self.__x+=self.__speed
            self.__fuel-=1
            self.__update_hitbox()
            self.__canvas.itemconfig(self.id, image=self.__skin_right)
            self.__repaint()
    def __create(self):
        self.id = self.__canvas.create_image(self.__x, self.__y, image = self.__skin_up, anchor='nw')
    def __repaint(self):
        self.__canvas.moveto(self.id, x=self.__x, y=self.__y)
    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)
    def intersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_ammo(self):
        return self.__ammo
    def get_model(self):
        return self.__model
    def get_hp(self):
        return self.__hp
    def get_xp(self):
        return self.__xp
    def get_fuel(self):
        return self.__fuel
    def get_speed(self):
        return self.__speed
    @staticmethod
    def get_count():
        return Tank.__count
    @staticmethod
    def get_size():
        return Tank.__SIZE
    def __str__(self):
        return (f'Модель: {self.__model}, Здоровье: {self.__hp},Топливо: {self.__fuel}, '
                     f'Опыт: {self.__xp}, Боекомплет: {self.__ammo}, '
                     f'Координаты: ({self.__x}, {self.__y})')