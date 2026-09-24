# Common Functions which is used in string, list, tuple, dictionary

print(len('Hello world'))

print(max('Hello world'))

print(min('Helloworld'))

print(sorted('Hello world',reverse=True))

# Capitalize / Tilte / Upper / Lower / Swapcase

s = 'hello world'
print(s.capitalize())

print(s.title())

print(s.upper())

print(s.lower())

print(s.swapcase())

# Count / Find / Index

a = 'My name is Khan'
print(a.count('a'))

print(a.find('is'))

print(a.index('is'))


# endswith / startswith
print(a.endswith('an'))
print(a.startswith('g'))

# Formate

name = 'Khan'
gender = 'Male'

print('Hi my name is {} and i am a {}'.format(name,gender))


# Split / Join

print(a.split())

print(' '.join(['My', 'name', 'is', 'Khan']))

# Replace

print('Hi my name is Khan'.replace('Khan','Qureshi'))

# Strip

print('Khan.                 '.strip())