''''def evencheck(num):
    if num % 2==0:
        print('even')
    else:
        print('odd')    
'''
from operator import truediv


def evencheck(num):
    r=num%2==0
    return r
r=evencheck(32)
#print(r)        
'''
#to return true if any no. is even insisde a list
def checkevenlist(list):
    for num in list:
        if num %2 ==0:
            return 'true' # once we return we will be out f function
        else:
            pass
    return 'False'         
a=checkevenlist([5,2,2])   
b=checkevenlist([5,3,29])   
print(a)
print(b)
          '''
#return all even no. in empty list
def checkeven(list):
    evenlist=[]
    for num in list:
        if num%2 ==0:
            evenlist.append(num)
        else:
            pass
    return evenlist
evenlist=[]
checkeven([2,7,8])    
print(evenlist)    
