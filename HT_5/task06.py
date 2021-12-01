#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.


def my_range(stop, start = 0, step = 1):
    if stop <= start:
        raise Exception("початок повинен бути менший за зупинку")
    i = start
    while i < stop:
        yield i
        i += step


for k in my_range(10):
    print(k)


