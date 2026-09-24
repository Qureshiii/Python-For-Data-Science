
a = int(input('Enter First Number: '))

b = int(input('Enter 2nd Number: '))

c = int(input('Enter Third Number: '))

if a==b==c:
        print('all the three numbers are same')
else:
    if a<b and a<c:
        print("Smallest is",a)

    elif b<a and b<c:
        print("Smallest is",b)

    else:
        print("Smallest is",c)
    