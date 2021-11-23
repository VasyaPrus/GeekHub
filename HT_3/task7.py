#калькулятор : повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculator(num_1, num_2, operation):
    if operation == "+":
        print(num_1 + num_2)
    elif operation == "-":
        print(num_1 - num_2)
    elif operation == "*":
        print(num_1 * num_2)
    elif operation == '/':
        if num_2 != 0:
            print(num_1 / num_2)
        else:
            print("Ділення на 0!")    
    else:
        print("Невірно введена операція")

calculator(5, 0, "/")
