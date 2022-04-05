#add digits to until we get single digit as op
n=1234
'''sum=0
while n>0 or sum>9:     #good approach
    if n==0:
        n=sum
        sum=0
    sum=sum+(n%10) 
    n=n//10   
    
print(sum)    
#print(a%10)'''
str=str(n)                #not a good approach
res=int(str[0])+int(str[1])+int(str[2])+int(str[3])
print(res)
