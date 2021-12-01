#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.


def my_range(start, stop, step = 1):
    i = start
    if step < 0 or step == 0:
        raise "Крок не повинен бути відємним числом і не дорівнювати нулю"
    if i > stop:
        while i > stop:
            yield i
            i -= step
    
    while i < stop:
        yield i
        i += step
    
try:
    for k in my_range(20, -8, 1):
        print(k)
except RuntimeError as ex:
    print(ex)
except:
    print("Сталася помилка")


