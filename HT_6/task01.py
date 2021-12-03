import time


def traffic_lights():
    
    light_cars = ['Red', 'Yellow', 'Green']
    
    while True:
        for i in range(4):
            print(light_cars[0], light_cars[2])
            time.sleep(1)
        for k in range(2):
            print(light_cars[1], light_cars[2])
            time.sleep(1)
        for j in range(4):
            print(light_cars[2], light_cars[0])
            time.sleep(1)
        for x in range(2):
            print(light_cars[1], light_cars[0])
            time.sleep(1)
        


traffic_lights()