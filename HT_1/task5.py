#Write a script to convert decimal to hexadecimal

num = int(input('Enter a decimal number: '))
num = hex(num)
num = str(num)
print('HexaDecimal value = ',num[2::] )