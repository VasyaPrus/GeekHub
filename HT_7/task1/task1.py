#1. Програма-банкомат.
#   Створити програму з наступним функціоналом:
#      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#   Особливості реалізації:
#      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#   Особливості функціонала:
#      - за кожен функціонал відповідає окрема функція;
#      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#      - потім - елементарне меню типа:
#        Введіть дію:
#           1. Продивитись баланс
#           2. Поповнити баланс
#           3. Вихід
#      - далі - фантазія і креатив :)
import json
data ={}
data['transactions'] = []


def start():
    def append_json(user, transaktion, sum):
        with open('username_transactions.json', 'w') as outfile:
            data['transactions'].append({
                'user' :f"{user}",

                f'{transaktion}': f"{sum}"
            })
            json.dump(data, outfile)

    def cash_withdrawal(login):
        with open("username_balance.json") as f1:
            templates = json.load(f1)
            append_balance = int(input('Сумма видачі готівки:'))
            if append_balance >= 0:
                for val in templates:
                    if val == login:
                        templates[val] -= append_balance 
                        if templates[val] <= - 501:
                            return print('максимальна сумма займу 500')
                        
                        with open("username_balance.json", "wt", encoding="utf-8") as f1:
                            append_json(login,' cash_withdrawal', append_balance) 
                            json.dump(templates, f1, indent=2)
                            print(templates[val])
                        
            else: print("Введена не коректна сумма")

    def see_balance(login):
        with open("username_balance.json") as f1:
            templates = json.load(f1)
            for val in templates:
                if val == login:
                    balance = templates[val]
                    print(balance)

    def replenish_the_balance():
        with open("username_balance.json") as f1:
            templates = json.load(f1)
            append_balance = int(input('Введіть значення поповнення:'))
            if append_balance >= 0:
                for val in templates:
                    if val == login:
                        templates[val] += append_balance
                        with open("username_balance.json", "wt", encoding="utf-8") as f1:
                            append_json(login,'replenish', append_balance) 
                            json.dump(templates, f1, indent=2)
                            print(templates[val])
            else: print('Введена не коректна сумма')
  
    with open("name.data") as f3:
        pairs = (line.split(",") for line in f3)
        users = {name:password.strip() for name, password in pairs}
    user = input("Введіть свій логін: ")
    passw = input("Введіть пароль: ")

    try:
        if passw == users[user]:
            login = user
            while True:
                print('1. Продивитись баланс\n2. Поповнити баланс\n3. Видача готівки\n4. Вихід')
                n = int(input(''))
                if n == 1:
                    see_balance(login)
                elif n == 2:
                    replenish_the_balance()
                elif n == 3:
                    cash_withdrawal(login)
                elif n == 4:
                    print('Дякую що залишаєтеся з нами)')
                    break
        else:
            print("Неправильний пароль")
    except KeyError:
        print("неправильне ім'я користувача або пароль")
                    

start()