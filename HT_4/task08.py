#8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. 
# Тобто, функція приймає два аргументи: список і величину зсуву 
# (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).

def shift(lst, shift):
    if shift < 0:
        steps = abs(shift)
        for i in range(shift):
            lst.append(lst.pop(0))
    else:
        for i in range(shift):
            lst.insert(0, lst.pop())
    print(lst, f"shift = {shift}")
 
shift([1,2,3,4,5], 1)


