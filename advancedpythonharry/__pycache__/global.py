'''
a=54
def func1():
    a=8
    print(a)
func1()
print(a)    '''

a=54
def func2():
    global a
    print(f'print statement 1 : {a}')
    a=8 #this line chnages global vakue of global a as a mentined inside a func
    print(f'print statement 2 : {a}')
func2()
print(f'print statement 3 : {a}')
    