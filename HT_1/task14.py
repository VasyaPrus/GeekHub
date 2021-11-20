N = int(input("Enter number:"))
dic = {}

for i in range(N+1):
    dic.update({i:i**2})

print(dic)