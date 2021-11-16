decimal_number = int(input("Enter decimal number: "))

y = decimal_number//16
x = decimal_number%16

if y>=16:
    z = y % 16
    y //= 16
    x %= 16
   
    
if (y == 10):
    y = "A"
if (y == 11):
    y = "B"
if (y == 12):
    y = "C"
if (y == 13):
    y = "D"
if (y == 14):
    y = "E"
if (y == 15):
    y = "F"

if (x == 10):
    x = "A"
if (x == 11):
    x = "B"
if (x == 12):
    x = "C"
if (x == 13):
    x = "D"
if (x == 14):
    x = "E"
if (x == 15):
    x = "F"

if (z == 10):
    z = "A"
if (z == 11):
    z = "B"
if (z == 12):
    z = "C"
if (z == 13):
    z = "D"
if (z == 14):
    z = "E"
if (z == 15):
    z = "F"    


result = str(y)+str(z)+str(x)

print(result)
