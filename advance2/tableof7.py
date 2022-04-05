#print table of 7 as vartical string
'''l=[str(i*7) for i in range(1,11)]

val="\n".join(l)
print(val)'''

#print no. divisible by 5 using filter func

'''l=[5,4,15,89,47,55,90]
a=filter(lambda a: a%5==0,l)
print(list(a))'''

#find max of list using reduce func
from functools import reduce
l=[1,5,8,46]
a=reduce(max,l)
print(a)