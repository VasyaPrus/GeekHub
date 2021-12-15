import sqlite3 as sq

with sq.connect('name.db') as con:
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
)""")



        

