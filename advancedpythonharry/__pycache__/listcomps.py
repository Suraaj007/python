# to slice a string into list
#note******
#we can also make dict comps and set comps
mystring= 'hello'
mylist=[]
'''for letter in mystring:
    mylist.append(letter)
print(mylist)'''

mylist=[i for i in mystring ] #we can put above logic in one line known as list comprehensions
print(mylist)

#eg of set
t=[1,4,2,4,1,2,3]
s={i for i in t}
print(s)


#to convert temp from celcius to fahrenheit
l=[]
celcius=[25,28,32]  
for temp in celcius:
    a=1.8* float(temp)
    fahrenheit=a+32.0
    l.append(fahrenheit)

print(l)

#To multiply two list no. in oreder
list1=[]
'''for x in [2,4,6]:
    for y in [10,20,30]:
        list1.append(x*y)
print(list1)'''
list1=[ i*j for i in [2,4,6] for j in [10,20,30] ] #listcomps
print(list1)
