# 1/1! + 2/2! + 3/3!..... till nth term

n = int(input("Enter nth Number: "))

result = 0
fact = 1

for i in range(1,n+1):
    fact = fact * i
    result = result + i/fact

print(result)
