#1. Програма-світлофор.
#   Створити програму-емулятор світлофора для авто і пішоходів.

#   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.

#   Кожну секунду виводиться поточні кольори.
#  Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.


import time


def traffic_lights():
    
    light = ['Red', 'Yellow', 'Green']
    
    while True:
        for i in range(4):
            print(light[0], light[2])
            time.sleep(1)
        for k in range(2):
            print(light[1], light[2])
            time.sleep(1)
        for j in range(4):
            print(light[2], light[0])
            time.sleep(1)
        for x in range(2):
            print(light[1], light[0])
            time.sleep(1)
        


traffic_lights()