#4. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), 
# кожен елемент якого буде ділитись без остачі на 5 але не буде ділитись на 3.

a = [i for i in range(101) if i % 5 == 0 and i % 3 != 0]
print(a)