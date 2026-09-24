# IF Else and Elif Statement

email = input('Enter Your Email: ')
password = input("Enter your Fucking password: ")

if email == 'mmuttahirqureshi@gmail.com' and password == '1234':
    print('Welcome to the system')

elif email == 'mmuttahirqureshi@gmail.com' and password != '1234':
    print('Invalid password')

elif email != 'mmuttahirqureshi@gmail.com' and password == '1234':
    print('Invalid email')        

else:
    print('Invalid email and password Both Fuck off')