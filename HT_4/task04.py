#4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.


def prime_list(start, stop):
    l = []
    for i in range(start, stop+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            l.append(i)
    print(l)

prime_list(10, 50)