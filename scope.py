#global

name= 'this is a global string'
def greet():
    #enclosing
    name='sammy'

    def hello():
        #local
        name='i am a local'
        print('hello'+ name)

    hello()

greet()    
x= 50
def func(x):
    print(f'x is {x}')
print(func(x))
