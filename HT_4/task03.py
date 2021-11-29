#3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.


def is_prime(N):
    for i in range(2, int(N / 2) + 1):
        if N % i == 0: 
            return False
        return True
            
            
print(is_prime(47))