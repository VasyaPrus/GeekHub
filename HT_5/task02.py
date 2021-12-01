#2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#  - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#  - щось своє :)
#   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.


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

check_log_pass('Vasya', 'Qwertyuio1')

