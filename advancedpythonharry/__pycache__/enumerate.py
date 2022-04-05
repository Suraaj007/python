list1=[3,53,2,False,6.2,'harry']
#enumerate func adds counter to an iterable and returns it
index=0
'''for item in a list1:
    print(item,index)
    index+=1'''
for index, item in enumerate(list1):
    print(item,index)