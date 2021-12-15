import sqlite3 as sq
import json

data = {'transactions': []}


def check(sum, collection_name ):
    with open(collection_name) as f:
        templates = json.load(f)
        for key in templates:
            if templates[key] > 0 and sum % int(key) == 0:
                return True
        return False


def restore_collection(dic, templates, withdrawal_balance, collection_name):
    for key in dic:
        while dic[key] != 0 and withdrawal_balance % int(key) != 0:
            dic[key] -= 1
            with open(collection_name, "wt", encoding="utf-8") as f:
                templates[key] += 1
                json.dump(templates, f, indent=2)


def start():
    def append_json(user, transaktion, sum):
        with open(f"{user}_transactions.json", 'w') as outfile:
            data['transactions'].append({
                'user': f"{user}",

                f'{transaktion}': f"{sum}"
            })
            json.dump(data, outfile)

    def cash_withdrawal(login):
        dic = {
            "1000": 0,
            "500": 0,
            "200": 0,
            "100": 0,
            "50": 0,
            "20": 0,
            "10": 0
        }
        with open("collection.json") as collection:

            templates = json.load(collection)
            withdrawal_balance = int(input('Введіть значення зняття:'))
            with open(f"{login}_balance.json") as f1:
                loc = json.load(f1)
                if (int(loc[login]) - int(withdrawal_balance)) <= -500:
                    print('максимальна сумма займу не більше 500')
                    return
            temp = withdrawal_balance
            full_sum = 0
            for key in templates:
                if int(templates[key]) > 0 and check(withdrawal_balance - int(key), "collection.json"):
                    while withdrawal_balance % int(key) != withdrawal_balance and templates[key] > 0:
                        withdrawal_balance -= int(key)
                        print(key)
                        full_sum += int(key)
                        dic[key] += 1

                        with open("collection.json", "wt", encoding="utf-8") as collection:
                            templates[key] -= 1
                            json.dump(templates, collection, indent=2)
        with open(f"{login}_balance.json") as f1:
            temp2 = json.load(f1)
            if full_sum != temp:
                restore_collection(dic, templates, withdrawal_balance, "collection.json")
                print("НЕМОЖЛИВО ЗНЯТИ ДАНУ СУМУ ЦІЛКОМ")

                return
            temp2[login] -= full_sum
            print("Було знято: ", temp)
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
                        append_json(login, 'replenish', append_balance)
                        json.dump(templates, f1, indent=2)
                        print(templates[val])
            else:
                print('Введена не коректна сумма')

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

    with sq.connect('name.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            password TEXT
        )""")
        for name, password in cur:
            print(name, password)
    user = input("Введіть свій логін: ")
    passw = input("Введіть пароль: ")

    try:
        if user == "Anya" and passw == "1111":
            collection()
        if passw == users[user]:
            login = user
            while True:
                print('1. Продивитись баланс\n2. Поповнити баланс\n3. Видача готівки\n4. Вихід')
                n = int(input(''))
                if n == 1:
                    see_balance(login)
                elif n == 2:
                    replenish_the_balance(login)
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


