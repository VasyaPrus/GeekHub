#Write a script to concatenate N strings.

N = int(input("Enter N :"))
l = []


while N > 0:
    l.append(input())
    N -= 1
    
print("".join(l))