#5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
#-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), 
#пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.


def check(x , y):
    if x > y:
        print("x більше за y на", x - y )
    elif x < y:
        print("y більше за x на", y - x)
    elif x == y:
        print("x дорівнює y")

check(32, 48)