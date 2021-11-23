#2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

initial_year = int(input("Enter initial year:"))
final_year = int(input("Enter final year:"))


for i in range(initial_year, final_year + 1):
    if i%400 == 0:
        print(i) 
    elif i%4 == 0 and i%100 != 0:
        print(i) 