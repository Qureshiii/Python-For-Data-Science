
# Print Unique pairs.

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)


# pattern 1.

# rows = int (input ('Enter Number of Rows: '))

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()    
    
# pattern 2.
row = int (input ('Enter Number of Rows: '))

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end='')
    
    for k in range(i-1,0,-1):
        print(k,end='')    
    print()