'''#write a program to print third fifth and seventh element in a list using enumerate function
l=[1,5,4,6,7,8,4,5,2,4]
for index,item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(f"the element at {index+1} position is {item}")


      '''

#accept 2 integers a and b and print a/b also when b=0 print infinite
try:
    a=int(input('enter a first no.'))
    b=int(input('enter a second no.'))
    print(a/b)
except ZeroDivisionError:
    print('infinite')
except:
    print('input error')