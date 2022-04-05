#bubble sort ,means comparing first no. with second one and putting highe no. at second positon
#we have to do the salong the list


l=[1,5,4,3,6,2,9,10,8]
i=0
n=len(l)-1
while i<n:
    a=l[i]
    b=l[i+1]
    if a>b:
        temp=l[i]
        l[i]=l[i+1]
        l[i+1]=temp

            
    else:
        pass
    i+=1
    
print(l)
print(i)