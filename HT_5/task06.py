#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.


def my_range(start, stop=None, step=1):
    if stop is not None:
        i = start
        if step > 0:
            while i < stop:
                yield i
                i += step
        elif step < 0 and i > stop:
            while i > stop:
                yield i
                i += step
        else:
            raise Exception("Передані некоректні аргументи")
    else:
        stop = start
        i = 0
        step = 1
        while i < stop:
            yield i
            i += step

print(list(my_range(15)))
print(list(my_range(1, 11)))
print(list(my_range(0, 30, 5)))
print(list(my_range(0, 10, 3)))
print(list(my_range(0, -10, -1)))
print(list(my_range(0)))
print(list(my_range(1, 0)))





