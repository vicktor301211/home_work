from hitbox import Hitbox
hb1 = Hitbox(0, 0,100 ,100)
hb2 = Hitbox(40, 0, 100, 100)
hb3 = Hitbox(120, 0, 100, 100)
int1 = hb1.intersects(hb2)
int3 = hb2.intersects(hb3)
int2 =hb1.intersects(hb3)
print('Взаимодействие хитбокса №1 и №2: ', int1)
print("Взаимодействие хитбокса №2 и №3: ", int3)
print("Взаимодействие хитбокса №1 и №3: ", int2)