#3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), 
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

def season(month):
    if month == 12 or month == 1 or month == 2:
        print("Зима")
    elif month == 3 or month == 4 or month == 5:
        print("Весна")
    elif month == 6 or month == 7 or month == 8:
        print("Літо")
    elif month == 9 or month == 10 or month == 11:
        print("Осінь")


season(7)    