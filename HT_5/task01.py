#1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).

class LoginException(Exception):
    pass
 
 
def check_log_pass(username, password, silent = False):
    dct = {'username1': 'pass1',
           'username2': 'pass2',
           'username3': 'pass3',
           'username4': 'pass4',
           'username5': 'pass5'}
    flag = dct.get(username, False) == password
    print(flag)
    if not flag and not silent:
        raise LoginException
    return flag

check_log_pass('username1','pass1')