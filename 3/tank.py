from tkinter import PhotoImage
from hitbox import Hitbox
from random import randint
import world
import texture as skin
class Tank:
    __count = 0
    #__SIZE = 85
# Инициализатор
    def __init__(self,canvas,x,y,ammo = 100, model = 'T - 14 Армата',speed = 10, bot = True):
        self.__bot = bot
        self.__target = None
        self.__hitbox = Hitbox(x, y, self.get_size(), self.get_size(), padding=1)
        self.__canvas = canvas
        Tank.__count+=1
        self.__model = model #моедль
        self.__fuel = 1000000000000
        self.__speed = speed
        self.__hp = 100 #здоровье
        self.__xp = 0 #опыт
        self.__ammo = ammo #боекомплект
        self.__x = x #положение по оси х
        self.__y = y #положение по оси у
        self.__vx = 0
        self.__vy = 0
        self.__dx = 0
        self.__dy = 0
        if self.__x < 0:
            self.__x=0
        if self.__y < 0:
            self.__y=0
        self.__create()
        self.right()

    def __check_map_collision(self):
        result = self.__hitbox.check_map_collision()
        if result:
            self.__undo_move()
            if self.__bot:
                self.__AI_change_orientation()
# Метод для остановки движения танка
    def stop(self):
        self.__vx = 0
        self.__vy = 0
        self.__dx = 0
        self.__dy = 0

# Метод для проверки столкновения с картой
    def __check_out_world(self):
        if self.__hitbox.left < 0 or \
                self.__hitbox.top < 0 or \
                self.__hitbox.right >= world.get_width() or \
                self.__hitbox.bottom >= world.get_height():
            self.__undo_move()
            if self.__bot:
                self.__AI_change_orientation()
# перезаправка танка
    def refuel(self):
            self.__fuel=1000
# Метод для определения цели танка
    def set_target(self, target):
        self.__target = target
# Метод движения бота за целью
    def __AI_goto_target(self):
        if randint(1, 2) == 1:
            if self.__target.get_x() < self.get_x():
                self.left()
            else:
                self.right()
        else:
            if self.__target.get_y() < self.get_y():
                self.forward()
            else:
                self.backward()
# Метод для перемещения бота
    def __AI(self):
        if randint(1, 50) == 1:
            if randint(1, 30)<29 and self.__target is not None:
                self.__AI_goto_target()
            else:
                self.__AI_change_orientation()
# Метод для поворота бота
    def __AI_change_orientation(self):
        rand = randint(0, 3)
        if rand == 0:
            self.left()
        if rand == 1:
            self.right()
        if rand == 2:
            self.forward()
        if rand == 3:
            self.backward()
# Метод стрельбы(пока не использован)
    def fire(self):
        if self.__ammo > 0:
            self.__ammo-=1
            print('стреляю')
        else:
            print('Нет снарядов')
# Метод для движения танка назад
    def backward(self):
        self.__vx = 0
        self.__vy = 1
        self.__canvas.itemconfig(self.id, image=skin.get('file_down'))
# Метод для движения танка вперед
    def forward(self):
        self.__vx = 0
        self.__vy = -1
        self.__canvas.itemconfig(self.id, image = skin.get('file_up'))
# Метод для поворота танка влево
    def left(self):
        self.__vx = -1
        self.__vy = 0
        self.__canvas.itemconfig(self.id, image=skin.get('file_left'))
# Метод для поворота танка вправо
    def right(self):
        self.__vx = 1
        self.__vy = 0
        self.__canvas.itemconfig(self.id, image=skin.get('file_right'))
    def start(self):
        self.__vx = self.__vx
        self.__vy = self.__vy
        if self.__vx == 1:
            self.__canvas.itemconfig(self.id, image=skin.get('file_right'))
        if self.__vx == -1:
            self.__canvas.itemconfig(self.id, image=skin.get('file_left'))
        if self.__vy == 1:
            self.__canvas.itemconfig(self.id, image=skin.get('file_down'))
        if self.__vy == -1:
            self.__canvas.itemconfig(self.id, image=skin.get('file_up'))
# Метоод обновления позиции танка и проверки столкновения с картой
    def update(self):
        if self.__fuel > self.__speed:
            if self.__bot:
                self.__AI()
            # self.__x += self.__vx * self.__speed
            # self.__y += self.__vy * self.__speed
            self.__dx = self.__vx * self.__speed
            self.__dy = self.__vy * self.__speed
            self.__x += self.__dx
            self.__y += self.__dy
            self.__fuel-= self.__speed
            self.__update_hitbox()
            self.__check_out_world()
            self.__check_map_collision()
            self.__repaint()
# Метод отмены последнего движения
    def __undo_move(self):
        if self.__dx == 0 and self.__dy == 0:
            return
        self.__x -= self.__dx
        self.__y -= self.__dy
        self.__fuel += self.__speed
        self.__update_hitbox()
        self.__repaint()
        self.__dx = 0
        self.__dy = 0
# Метод для создания танка
    def __create(self):
        self.id = self.__canvas.create_image(self.__x, self.__y, image = skin.get('file_up'), anchor='nw')
# Метод для передвижения танка на экране
    def __repaint(self):
        self.__canvas.moveto(self.id, x=world.get_screen_x(self.__x), y=world.get_screen_y(self.__y))
# Метод для обновления хитбокса танка
    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)
# Метод для проверки столкновения с другим танком
    def intersects(self, other_tank):
        value = self.__hitbox.intersects(other_tank.__hitbox)
        if value:
            self.__undo_move()
            if self.__bot:
                self.__AI_change_orientation()
        return value
# Геттеры для свойств танка
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
    #@staticmethod
    def get_size(self):
        return skin.get('file_up').width()
# Метод для вывода информации о танке пока не использован)
    def __del__(self):
        print(f'танк удалён')
        Tank.__count -= 1
        try:
            self.__canvas.delete(self.id)
        except Exception:
            pass
    def __str__(self):
        return (f'Модель: {self.__model}, Здоровье: {self.__hp},Топливо: {self.__fuel}, '
                     f'Опыт: {self.__xp}, Боекомплет: {self.__ammo}, '
                     f'Координаты: ({self.__x}, {self.__y})')