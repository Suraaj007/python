'''l=[]
n=3
for i in range(1,n+1):
    l.append("*"*i)
print('\n'.join(l))'''
'''n=3
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ") #bcz of for loop om every iteration utput will be in printed in new line
#so to get more than 1 star on same line we use end keyword which put end as per our need at end of evry iteration
    print("\n")  '''

#2
n=5
  #aint working lol
for i in range(0,n):
    k=n-i  #k here used to print req spaces
    for j in range(0,k):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end="")
    print("\n")    
'''n=3   
for i in range(0,n):
    for j in range(0,n-i):
        print("*",end=" ")    
    print("\n")  '''