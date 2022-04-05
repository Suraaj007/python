def greet(name):
    print(f'Good morning {name}')
print(__name__)  #name evaluates name of module  from where file running

if __name__=="__main__":   #this line is useful when we want to use only particular func in another file as it becomes false and below code stops
    n=input('Enter a name\n')
    greet(n)