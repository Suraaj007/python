
dict={}
l=int(input('no. of playrs'))
for _ in range(l):
    name = input('enter a name')
    score = float(input('enter his score'))
    dict[name]=[score]  
    
print(dict)   