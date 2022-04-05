'''string=input('enter a username')
if len(string)>10:
    print('more than 10 char')
else:
    print('less than 10 char')    '''

'''a=int(input('enter your marks')) 
if 100>a>=90:
    print('grade Ex')   
elif 90>a>=80:
    print('grade A' )
elif 80>a>=70:
    print('grade B' )     
elif 70>a>=60:
    print('grade C' ) 
elif 60>a>=50:
    print('grade D' )     
elif a<50:
    print('grade F' ) 
else:
    print('wrong input')  '''

'''a=10
#print((i*a) for i in range(1,11))          #erorrrrr      
#for i in range(1,11):
    #print(a*i)
i=1   
while i in range(1,11):
    print(a*i)
    i+=1'''
'''
b=0

if b==1 or b==0:
    print('not a prime no')    
else:
    i=b
    for i in range(2,i):
        if b%i==0:
            print('not  a prime')
            break
    else:
        print('prime no. hai ye bhai')'''


#sum of n natural no.
'''sum=0
i=1
n=10
while i<=n:
    sum=sum+i
    i+=1
print(sum)'''

#factorial using for loop
'''fact=1
n=10
for i in range(1,n+1):
    fact*=i
print(fact)    
'''
#Q8

'''n=3
for i in range(0,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print('\r')    '''
#to get all name starting with s in a list
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)    
      
    




