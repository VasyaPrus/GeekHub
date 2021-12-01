#3. На основі попередньої функції створити наступний кусок кода:
#   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
def check_log_pass(username, password):
    if len(username) < 3 or len(username) > 50:
        raise Exception("Ім'я користувача повинно містити 3-50 символів")
    if password.islower():
        raise Exception ("Пароль повинен мати велику літеру")
    elif len(password) < 8:
        raise Exception ("Пароль повинен містити більше 8-ми символів")
    for letter in password:
        if letter.isdigit():
            break
    else:
        raise Exception('пароль повинен мати хоча б одну цифру')

def check():
    list_user_pass = [['username1', 'Pass1'],['username2', 'pass2'], ['username3', 'pajbfjbfJJs2']]
    for i in list_user_pass:
        try: 
            check_log_pass(i[0], i[1])
            print("Name: ", i[0])
            print("Password: ", i[1])
            print("STATUS: OK")
        except Exception as e:
            print("Name: ", i[0])
            print("Password: ", i[1])
            print("Status: ", e)
            

               


check()