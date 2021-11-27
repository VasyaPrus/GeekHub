#6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.

def check_number(num):
    if num > 0:
        return num * num
    elif num < 0:
        return num + 100
    else:
        return num

print(check_number(4))