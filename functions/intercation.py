'''#shufling
example= [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)
'''
 #three cup monnte
from unittest import result


def shuffle_list(mylist):
    from random import shuffle
    shuffle(mylist)
    return mylist


mylist= ['','o','']
shuffle_list(mylist)
result= shuffle_list(mylist)

def plyr_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('enter your guess position from 0,1,2')
    return int(guess)
#plyr_guess()        
myindex= plyr_guess()
print(myindex)

def checkguess(mylist,myindex):
   if  mylist[myindex]==0:
       print('whoila!!! correct guess')
   else:
       print('wrong guess!')   

checkguess(mylist,myindex)