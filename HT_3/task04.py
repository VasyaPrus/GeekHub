#4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. 
# Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. 
# Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def sum_numbers(num_1, num_2):
    return num_1 + num_2

def multiply_numbers(num_1, num_2):
    return num_1 * num_2

def square_numbers(num_1):
    return num_1 ** 2

def general_function(num_1, num_2):
    print(sum_numbers(num_1, num_2))
    print(multiply_numbers(num_1, num_2))
    print(square_numbers(num_1))
    return num_2 - num_1
    
print(general_function(8, 12))