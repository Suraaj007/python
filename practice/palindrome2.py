#check whether palindrome is possible by rearranging the string
str='nitin'
n=len(str)
print(len(str))
l=[]
'''for i in range(n):
    if str[i] in l:
        l.remove(str[i])
    else:
        l.append(str[i])'''
for i in str:
    if i in l:
        l.remove(i)
    else:
        l.append(i)            
print(len(l))        
if n%2==0:

    if len(l)==0:
        print('it can be palindrome')            
    else:
        print('not a palindrome')  
else:
    if len(l)==1:
        print('it can be palindrome')
    else:
        print('not a palindrome')                  
