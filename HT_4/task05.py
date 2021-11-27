def fibonacci(n):
    fib1 = 1
    fib2 = 1
    print(fib1, fib2, end=" ")
    
    
    for i in range(2, n+1):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=" ")

fibonacci(10)