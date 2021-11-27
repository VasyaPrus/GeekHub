#3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.


def is_prime(N):
    for i in range(2, N+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            print(i)


is_prime(50)