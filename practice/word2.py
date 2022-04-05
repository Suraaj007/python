
#read and display ddmmyyyy forat
'''str=input('enter a date in ddmmyyyy')
print(f'date is{str[:2]}')
print(f'month is{str[2:4]}')
print(f'year is{str[4:]}')

#write a program to count vowels from given word
word=input('enter a word\n')
count=0
l=['a','e','i','o','u']
for i in word:
    if i in l:
        l.remove(i)
        count+=1
print(f'no. of vowels {count}')

#write a program to count no. of times particular vowels 
# occur from given word
word=input('enter a word\n')
count=0
l1=['a','e','i','o','u']
l2=[]
for i in word:
    if i in l1:
        l2.append(i)
        

count1=l2.count('u')
print(f'u appears {count1}')

#wap to print sum of even and odd location in a no.
s='4567'
a=(s[::2])
b=int(a)
print(a)
sum1=0
sum2=0
for i in range(len(a)):
    sum1+=(b%10)
    b=b//10
print(sum1)


c=s[1::2]
d=int(c)
print(d)
for j in range(len(c)):
    sum2+=(d%10)
    d=d//10
print(sum2)

#find min max and sum of digit given
n=8265
l=[]
while n>0:
    a=n%10
    l.append(a)
    n=n//10
m=max(l)    
print(m)
k=min(l)    
print(k)

#to delete particulr letter in a string
str1='moon'
str2=' o'
l=[]
if 'o' in 'moon':
    l=str1.split('o')
print(''.join(l)) '''


count=0
a=input('enter a word:  ')
b=input('enter a sentences :   ')
l=[]
l=b.split(" ")
print(len(l)) 
for  a in l:
    print(a)
    # count+=1
    # l.remove(a)
print(f' the given word appears {count} times')


