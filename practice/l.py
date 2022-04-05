
print("Hello World")
while True:
    n=int(input('eneter no. of hours\n'))
    if 1<=n<=25:
        
        break
    else:
        continue
i=1
l1=[]
l2=[]
l3=[]
c=0
while i<=n:
    a=int(input(f'eneter a no. of guest  eneterd at {i} hour\t'))
    
    b= int(input(f'eneter a no. of guest  left at {i} hour\t'))
    
    if 0<=a<= 500 and 0<=b <=500:
        l1.append(a)
        l2.append(b)
        c=c+a-b
        l3.append(c)
        i+=1
    else:
        continue
        
        


    
    
print(max(l3))
    
