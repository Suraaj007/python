#to find vol of a cube
def vol(r):
    volume = (4/3)*3.141*(r*r*r)
    print(volume)
vol(1)   

def multiply(list1):
    ans=1
    for i in list1:
        ans=ans*i
    print(ans)    
        


list1=[1,2,3,-4,5]
multiply(list1)

some= 'a'
print(some.islower())