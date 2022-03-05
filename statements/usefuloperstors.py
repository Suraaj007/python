#mylist=[1,2,3]
for num in range(3,10):
    print(num)

for num in range(10):
    print(num)

for num in range(1,10,3):   #include first excude second stepsize third
    print(num)

print(list(range(0,11,2)))
count=0
for letter in "abcde":
    print(f'at index {count} letter is {letter}')
    count+=1

word='abcde'
for item  in enumerate (word):
    print(item)

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

list1=[1,2,3]
list2=["a","b","c"]    
list3=[100,200,300]
for item in zip(list1,list2,list3):
    print(item)

print(list(zip(list1,list2)))    

print('x'in [1,2,3])
print('x' in ['x','y','z'])

dict={'mykey':345}
print(345 in dict.values())
print(345 in dict.keys())


list5=[5,60,84,56]
print(list5)
print(min(list5))
print(max(list5))


from random import shuffle #not workinggggggggg
list6=[5,9,4,6,3]
shuffle(list6)
print(list6)

from random import randint
print(randint(0,100))


