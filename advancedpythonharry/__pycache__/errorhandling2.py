try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('eroor occurs')


#2
try:
    x=5
    y=0
    z=x/y
except:
    print('zerodivisionerror')
finally:
    print('all done')        
'''
#3
def ask():
    while True:
        try:
            n=int(input('enter a no.'))
        except:
            print('please try again\n')
            continue
        else:
            break       
    print('your no. squared is:')
    print(n**2)     
ask()    
'''

#4
def ask():
    waiting=True
    while waiting:
        try:
            n=int(input('enter a no.'))
        except:
            print('please try again\n')
            continue
        else:
            waiting=False       
    print('your no. squared is:')
    print(n**2)     
ask()    