#to check if 3 appears  twice consecutively in a list 
list1=[1,2,3,3,5]
list2=[3,1,5,4]
def func(num):
    for i in range(0,len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
func(list2)
print(func(list2))