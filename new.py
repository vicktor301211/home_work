class Animal:
    def speak(self):
        print('*Издаёт звуки*')
class Dog(Animal):
    def speak(self):
        print('Гав-гав!')
class Dog_small(Dog):
    def speak(self):
        print('Тяф-тяф!')
class Big_dog(Dog):
    def speak(self):
        print('ГАВ-ГАВ!')
class Toy_small_dog(Dog_small):
    def speak(self):
        print('Игрушка звучит как гав-гав')
class Robot_sobaka(Toy_small_dog):
    def speak(self):
        print('Робот звучит как гав-гав')
class Big_evil_dog(Big_dog):
    def speak(self):
        super().speak()
        print('Злой взгляд!!')
        print("Хмурится")
class Cat(Animal):
    def _meow(self):
        print('Мяу-мяу!')
    def speak(self):
        self._meow()
class Fat_cat_vaska(Cat):
    def _meow(self):
        print('МЯУ! ХОЧУ ЕСТЬ!')
animal = Animal()
animal.speak()
print('______________________________________________________________________________________________')
dog = Dog()
dog.speak()
print('______________________________________________________________________________________________')
small_dog = Dog_small()
small_dog.speak()
print('______________________________________________________________________________________________')
big_dog = Big_dog()
big_dog.speak()
print('______________________________________________________________________________________________')
toy = Toy_small_dog()
toy.speak()
print('______________________________________________________________________________________________')
robot = Robot_sobaka()
robot.speak()
print('______________________________________________________________________________________________')
evil_dog = Big_evil_dog()
evil_dog.speak()
print('______________________________________________________________________________________________')
cat = Cat()
cat.speak()
print('______________________________________________________________________________________________')
fat_cat_vaska = Fat_cat_vaska()
fat_cat_vaska.speak()
print('______________________________________________________________________________________________')
def say_n_time(animal, time):
    for _ in range(time):
        animal.speak()
druzhok = Big_evil_dog()
say_n_time(druzhok, 3)
print('______________________________________________________________________________________________')
say_n_time(fat_cat_vaska, 5)
print('______________________________________________________________________________________________')
list_of_animal = [Cat(), Dog(), Fat_cat_vaska(), Big_evil_dog()]
for animal in list_of_animal:
    animal.speak()
print('______________________________________________________________________________________________')
for animal in list_of_animal:
    say_n_time(animal,2)
    print('______________________________________________________________________________________________')
