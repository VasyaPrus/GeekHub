#Write a script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

N = int(input("Enter number:"))
dic = {}


for i in range(N+1):
    dic.update({i:i**2})

print(dic)