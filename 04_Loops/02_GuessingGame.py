import random

jackpot = random.randint(1,100)


guess = int(input("Enter Your Guess: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print('Go Higher! This is low.')
    else:
        print('Go Lower! This is high')

    guess = int(input("Enter Your Guess: "))
    counter = counter + 1
else:
    print("Correct Guess! ")
    print('Attempts',counter)