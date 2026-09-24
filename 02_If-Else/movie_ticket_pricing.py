# Movie Ticket Pricing by age

age = int(input("Enter your age to check a ticket price: "))

if age < 4:
    print("your ticket is Free!")
    
elif age <=12:
    print("Child ticket: 5$")
    
elif age <=60:
    print ("Adult ticket: 10$")
    
else:
    print('Senior citizen discount ticket: 7$')