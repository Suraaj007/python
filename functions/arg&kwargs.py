from ast import arg
'''

def myfunc(a,b):
    return (a+b)*.1
x=myfunc(40,60)    
print(x)

def func(*args):
    print(args)
    print((sum(args)*.1))
    for item in args:
        print(item)
func(10,30,30,20,10)    

def func1(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit choice is {}'.format( kwargs['fruit']))
    else:
        print('i didnt find any fruit here')
func1(fruit='apple', veggie='lettuce')
'''

def func2(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like {}{}'.format(args[0], kwargs['food']))
func2(20,30,50,food='eggs',fruit='jamon')    