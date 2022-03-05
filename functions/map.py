'''def square(num):
    return num**2
mynum=[1,2,3,4,5]
for items in map(square,mynum):
    print(items)    
print(list(map(square,mynum)) )  #map applies func to every element in the list

def splicer(mystr):
    if len(mystr)%2==0:
        return 'even'
    else:
        return mystr[0]    
names=['andy','sally','eve']
print(list(map(splicer,names)))

#filter3#############
def checknum(mynum):
    return mynum%2== 0
mynum=[1,2,3,4,5,6]
print(list(filter(checknum,mynum)))    
for n in filter(checknum,mynum):
    print(n)

'''
 #lambda func##################
'''def square(num):
     return num**2
     return result
print(square(3))
'''















