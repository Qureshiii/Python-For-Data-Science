

email = input('Enter your email: ')
password = input('Enter your password: ')

if email == 'mmuttahirqureshi@gmail.com' and password == '123':
    print('Welcome')
elif email == 'mmuttahirqureshi@gmail.com' and password != '123':
    print("Incorrect Password")
    password = input('Enter password again: ')
    
    # Nested if-else Used here
    
    if password == '123':
        print('Welcome Finally!')
    else:
        print("Shut the fuck up")

elif email != 'mmuttahirqureshi@gmail.com' and password == '123':
    print('Incorrect Email')
    email = input('Enter your Correct Email: ')
    
    # Nested if-else used here
    
    if email == 'mmuttahirqureshi@gmail.com':
        print('Welcome Finally!')
    else:
        print('Tum se na ho payega beta!')
        
else:
    print('Not Correct')                