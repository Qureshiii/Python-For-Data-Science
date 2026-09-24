
# find the sum of three digit number.


number = int(input('Enter 3 digit number'))
# 345

a = number % 10
# 345%10 -> 5 (modulus is used to do a division and give you the reminder)
number = number//10
# 345//10 -> 34 (integer division is used to throne away the reminder)

b = number % 10
# 34%10 -> 4
number = number//10
# 34//10 -> 3

#c = number % 10
c = number
# 3%10 -> 3

print(a+b+c)


               