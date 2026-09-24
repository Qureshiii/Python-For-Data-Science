# find the length of the given string without using len() function.

s = input('Enter the string: ')

counter = 0

for i in s:
    counter = counter + 1

print('lenght of string is: ',counter)


# Extract username from a given email.
# eg. if the email is nitish24singh@gmail.com
# then the email should be nitish24singh

a = input('Enter the Email: ')

position = a.index('@')

print(a[0:position])

#Count the frequency of a particular character in a provided string.
#eg. 'hello how are you' is the string the frequency of h in this string is 2.

b = input('Enter the string: ')

term = input('what would you like to search for: ')

counter = 0

for i in b:
    if i == term:
        counter = counter + 1
        
print('Frequency',counter)



#write a program which can remove a particular character from a string.


c = input('Enter the string: ')

chara = input('what would you like to remove: ')

result = ''
for i in c:
    if i != chara:
        result = result + i

print(result)


#Write a program that can check whether the given string are palindrome are not?
# palindromes are (madam,level,radar,civic,mom,dad,noon) these are the palindromes

d = input('Enter a word: ')

flag = True

for i in range(0,len(d)//2):
    if d[i] != d[len(d) -i -1]:
        flag = False
        print('not a pallindrome!')
        break
    
if flag:
    print('pallindrome')
    


#write a program to count the number of words in a string without split()

e = input('Enter a String: ')
l = []
temp = ''

for i in e:
    if i != ' ':
        temp = temp + i
    else:
        l.append(temp)
        temp = ''
l.append(temp)
print(l)



#write a program to convert a string to title case without using title()

f = input('Enter a String: ')

l=[]

for i in f.split():
    l.append(i[0].upper() + i[1:].lower())
    
print(' '.join(l))    


