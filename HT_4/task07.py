#7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def check_elements(l_string):
    l = []
    

    for i in l_string:
        for j in i:
            l.append(j)
    check_set = set(l)
    result={}
    
    
    for i in check_set:
        result[i] = l.count(i)
    print(result)


check_elements(['aaa111ka1kk'])