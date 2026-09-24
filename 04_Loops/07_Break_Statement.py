
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)
    


rang = int(input("Enter Value: "))

for i in range(1,rang+1):
    for j in range(2,i):
        if i % j == 0:
            break
            print('Prime Number')
    else:
        print(i)
           