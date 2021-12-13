#1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
#   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
#   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
#   Особливості реалізації:
#   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
#   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
#     - переглянути наявні купюри;
#     - змінити кількість купюр;
#   - видача грошей для користувачів відбувається в межах наявних купюр;
#   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.

import json
data ={}
data['transactions'] = []

def start():
    def append_json(user, transaktion, sum):
        with open(f"{user}_transactions.json", 'w') as outfile:
            data['transactions'].append({
                'user' :f"{user}",

                f'{transaktion}': f"{sum}"
            })
            json.dump(data, outfile)

    def cash_withdrawal(login):
        with open("collection.json") as f:
            templates = json.load(f)
            withdrawal_balance = int(input('Введіть значення зняття:'))
            temp = withdrawal_balance
            full_sum = 0
            dic = {
                    "1000": 0,
                    "500": 0,
                    "200": 0,
                    "100": 0,
                    "50": 0,
                    "20": 0,
                    "10": 0
                    }
            for key in templates:
                if int(templates[key]) > 0:
                    while withdrawal_balance % int(key) != withdrawal_balance and withdrawal_balance % int(key) >= 0 and templates[key] > 0:
                        withdrawal_balance -= int(key)
                        full_sum += int(key)
                        dic[key] += 1

                        with open("collection.json", "wt", encoding="utf-8") as f:
                            templates[key]-= 1 
                            json.dump(templates, f, indent=2)
        with open(f"{login}_balance.json") as f1:
            temp2 = json.load(f1)
            if(full_sum != temp):
                for key in dic:
                    while dic[key] != 0:
                        dic[key] -=1
                        with open("collection.json", "wt", encoding="utf-8") as f:
                            templates[key]+= 1 
                            json.dump(templates, f, indent=2)
                print("НЕМОЖЛИВО ЗНЯТИ ДАНУ СУМУ ЦІЛКОМ")

                return
            temp2[login] -= full_sum
            print("Було знято: ", temp)
            if temp2[login] <= -501:
                    return print('максимальна сумма займу не більше 500')
            with open(f"{login}_balance.json", "wt", encoding="utf-8") as f1:
                json.dump(temp2, f1, indent=2)
            append_json(login, "withdrawal", full_sum)

                    
            
    def replenish_the_balance(login):
        with open(f"{login}_balance.json") as f1:
            templates = json.load(f1)
            append_balance = int(input('Введіть значення поповнення:'))
            if append_balance >= 0:
                for val in templates:
                    templates[val] += append_balance
                    with open(f"{login}_balance.json", "wt", encoding="utf-8") as f1:
                        append_json(login,'replenish', append_balance) 
                        json.dump(templates, f1, indent=2)
                        print(templates[val])
            else: print('Введена не коректна сумма')
    
    
    def see_balance(login):
        with open(f"{login}_balance.json") as f1:
            templates = json.load(f1)
            for val in templates:
                if val == login:
                    balance = templates[val]
            print(balance)

    def collection():
        
        def check_banknotes():
            for k, v in templates.items(): 
                print(f'Валюта:{k},Кількість валюти:{v}')
            collection()

        def change_number_banknotes():
            par = int(input('Введіть номінал купюри:'))
            number = int(input('Введіть кількість купюр:'))
            for kay_par in templates:
                if int(kay_par) == par:
                    templates[kay_par] += number
                    with open("collection.json", "wt", encoding="utf-8") as f:
                        json.dump(templates, f, indent=2)
            collection()
        with open("collection.json") as f:
            templates = json.load(f)
            print('1. Переглянути наявні купюри\n2. Змінити кількість купюр\n3. Вийти')
            n = int(input(''))
            if n == 1:
                check_banknotes()
            elif n == 2:
                change_number_banknotes()
            elif n == 3:
                raise SystemExit 
                
                
    with open("name.data") as f3:
        pairs = (line.split(",") for line in f3)
        users = {name:password.strip() for name, password in pairs}
    user = input("Введіть свій логін: ")
    passw = input("Введіть пароль: ")

    try:
        if user == "Anya" and passw == "1111":
            collection()
        if passw == users[user]:
            login = user
            while True:
                print('1. Продивитись баланс\n2. Поповнити баланс\n3. Видача готівки\n5. Вихід')
                n = int(input(''))
                if n == 1:
                    see_balance(login)
                elif n == 2:
                    replenish_the_balance(login)
                elif n == 3:
                    cash_withdrawal(login)
                elif n == 5:
                    print('Дякую що залишаєтеся з нами)')
                    break
        
            
        else:
            print("Неправильний пароль")
    except KeyError:
        print("неправильне ім'я користувача або пароль")
        
start()