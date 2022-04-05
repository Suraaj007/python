#key diff bw tuple and list is tuples are immutable where as list are mutable
t=(1,2,3,3,3,3)
print(type(t))

print(len(t))
print(t[0])
k=('a','a','b','c')

#to count no of times variable  or value rpeated
print(k.count('a'))
print(t.count(3))
#to know the index position by default it returns position at which that variable occur first
print(k.index('a'))
l=[5,6,6,3,2,1]
print(l.count(6))