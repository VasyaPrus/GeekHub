#калькулятор : повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator(num_1, num_2, operation):
    if operation == "+":
        print(num_1 + num_2)
    elif operation == "-":
        print(num_1 - num_2)
    elif operation == "*":
        print(num_1 * num_2)
    elif operation == "/":
        print(num_1 / num_2)    
    else:
        print("Невірно введяна операція")

calculator(15, 3, "+")
