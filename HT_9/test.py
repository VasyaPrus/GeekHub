import sqlite3 as sq


'''with sq.connect('name.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name varchar(255),
    balance varchar money,
    password varchar(255),
    transactionID int
)""")


        cur.execute("""CREATE TABLE IF NOT EXISTS Colection (
    nominal int,
    count int
)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS transaction_Users (
    transactionId  int,
    allTransaction string
)""")'''




def start():   
    def cash_withdrawal():
        dic = {
            "1000": 0,
            "500": 0,
            "200": 0,
            "100": 0,
            "50": 0,
            "20": 0,
            "10": 0
        }
        withdrawal_balance = int(input('Введіть значення зняття:'))
        cur.execute('SELECT nominal, count FROM Colection WHERE name = ?',(user,))
        cur.close()



    def replenish_the_balance():
        with sq.connect('name.db') as con:
            cur = con.cursor()
            append_balance = int(input('Введіть значення поповнення:'))
            cur.execute('SELECT balance FROM users Where name = ?', ("v",))
            result = int(cur.fetchone()[0]) + append_balance
            cur.execute("UPDATE users SET balance = ? WHERE name = 'v'", (result, ))
    
    def see_balance():
        with sq.connect('name.db') as con:
            cur = con.cursor()
            cur.execute('SELECT balance FROM users WHERE name = ?',(user,))
            result = int(cur.fetchone()[0])
            print(result)
    
    with sq.connect('name.db') as con:
        cur = con.cursor()
        temp_user_data = cur.execute("SELECT name, password FROM users ")
    user = input("Введіть свій логін: ")
    pas = input("Введіть пароль: ")

    for name, password in temp_user_data:
        if name == user and password == pas:
            while True:
                print('1. Продивитись баланс\n2. Поповнити баланс\n3. Видача готівки\n4. Вихід')
                n = int(input(''))
                if n == 1:
                    see_balance()
                elif n == 2:
                    replenish_the_balance()
                elif n == 3:
                    cash_withdrawal()
                elif n == 4:
                    return print('Дякую що залишаєтеся з нами)')


    else:
        print("Неправильний пароль або логін")





start()




        

