


def myfunc(a,b):
    return (a+b)*.1
x=myfunc(40,60)    
print(x)

#if we arent sure about how many no. user gonna enterd its safer to use args
def func(*args):
    print(args)
    print((sum(args)*.1))
    #for item in args:
        #print(item)
func(10,30,30,20,10)
func(10,50,40)

#kwargs are used when we have key value pairs as inputs
def func1(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit choice is {}'.format( kwargs['fruit']))
    else:
        print('i didnt find any fruit here')
func1(fruit='apple', veggie='lettuce')

# in args we define position to access whereas in kwargs we define key to access values
def func2(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like {}{}'.format(args[0], kwargs['food']))
func2(20,30,50,food='eggs',fruit='jamon')    