#Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> 
#Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#-  якщо довжина бульше 50 - > ваша фантазiя (сортує букви в порядку зростання та окремо числа)

def check_str(string):
    letters = "".join(filter(lambda x: not x.isdigit(), string))
    numbers = "".join(filter(str.isdigit, string))
    l = []
    
    if 30 <= len(string) <= 50:
        print("Кількість букв:",len(letters), "\nКількість цифр:", len(numbers))
    
    elif 30 > len(string):
        for i in numbers:
            i = int(i)
            l.append(i)
        print("Сумма всіх чисел:",sum(l), "\nРядок з буквами:", letters)

    elif 50 < len(string):
        print("Букви в порядку зростання:", "".join(sorted(letters)))
        print("Числа в порядку зростання:", "".join(sorted(numbers)))

check_str("f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345")

