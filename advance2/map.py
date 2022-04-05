from cgi import print_arguments
from re import L


def square(num):
    return num**2
mynum=[1,2,3,4,5]
for items in map(square,mynum):
    print(items)    
#print(list(map(square,mynum)) )  #map applies func to every element in the list
print(list(map(lambda x:x*x,mynum)))  #lambda use




def splicer(mystr):
    if len(mystr)%2==0:
        return 'even'
    else:
        return mystr[0]    
names=['andy','sally','eve']
print(list(map(splicer,names)))

#filter3#############
def checknum(mynum):
    return mynum%2== 0 #filter function return t or f and acc. we get filtered out list
mynum=[1,2,3,4,5,6]
print(list(filter(checknum,mynum)))    
for n in filter(checknum,mynum):
    print(n)


 #reduce func##################  to educe the lines of program
from functools import reduce
list1=[1,2,3,4]
sum= reduce(lambda x,y:x+y,list1)
















