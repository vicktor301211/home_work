import world
class Hitbox:
# Инициализируем Hitbox с позицией и размерами
    def __init__(self, x, y, width, height, padding=0):
        self.pad = padding
        self.__x = x
        self.__y = y
        self.__set_width(width)
        self.__set_height(height)
        self.__black_list = [world.CONCRETE, world.BRICK, world.WATER]

    def __get_corner_points(self):
        p_top_right = {'x': self.right, 'y': self.top}
        p_top_left = {'x': self.left, 'y': self.top}
        p_bottom_left = {'x': self.left, 'y': self.bottom}
        p_bottom_right = {'x': self.right, 'y': self.bottom}
        return [p_top_right, p_top_left, p_bottom_left, p_bottom_right]

    def check_map_collision(self, details):
        for point in self.__get_corner_points():
            row = world.get_row(point['y'])
            col = world.get_col(point['x'])
            block = world.get_block(row, col)
            if block in self.__black_list:
                details['block'] = block
                details['col'] = col
                details['row'] = row
                return True
        return False

    def __get_width(self):
        return self.__width
    def __set_width(self, width):
        if width <0:
            width=0
        self.__width = width
    def __get_height(self):
        return self.__height
    def __set_height(self, height):
        if height <0:
            height=0
        self.__height = height
    def __get_x(self):
        return self.__x
    def __set_x(self, x):
        self.__x = x
    def __get_y(self):
        return self.__y
    def __set_y(self, y):
        self.__y = y

# Геттеры и сеттеры для сторон хитбокса
    def __get_top(self):
        return self.y + self.pad
    def __get_bottom(self):
        return self.y+self.height-self.pad
    def __get_left(self):
        return self.x+self.pad
    def __get_right(self):
        return self.x+self.width-self.pad
# Метод для передвижения хитбокса к новым координатам
    def moveto(self, x, y):
        self.__set_x(x)
        self.__set_y(y)
# Метод для движения хитбокса
    def move(self, dx, dy):
        self.__set_x(dx+self.__get_x())
        self.__set_y(dy + self.__get_y())
# Метод для проверки пересечения хитбокса с другим хитбоксом
    def intersects(self, other):
        if self.left > other.right:
            return False
        if self.right < other.left:
            return False
        if self.top > other.bottom:
            return False
        if self.bottom < other.top:
            return False
        return True
    x  = property(__get_x, __set_x)
    y = property(__get_y, __set_y)
    width = property(__get_width, __set_width)
    height = property(__get_height, __set_height)

    top = property(__get_top)
    bottom = property(__get_bottom)
    left = property(__get_left)
    right = property(__get_right)
    def __str__(self):
        return (f'({self.__x=}, {self.__y=}, {self.__width=}, {self.__height=})')