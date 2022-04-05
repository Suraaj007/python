#make range function which include both high and low value inclusives



def rnge(low,num,high):
    if num in range(low,high+1):
        print(' in range')
    else:
        print('not in range')    
rnge(2,5,7)

#accept a string from user and count no. of uppercase and lowercase letter
def func(string1):
    uppercase=0
    lowercase=0
    
    for letter in string1:
    
        if letter.islower():
            uppercase+=1
        elif letter.isupper():
            lowercase+=1
        else:
            pass
    print(f'my string is {string1}')    
    print(f'count of uppercase letters{uppercase}') 
    print(f'count of lowercase letters{lowercase}')  
func('Hello') 

print('hello'.isupper()   )      
    