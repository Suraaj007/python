# write a func to take two word strings and return true if both words begin with same letter
def func(str1):
    mylist=str1.split()
    if mylist[0][0]==mylist[1][0]:
        print('true')
    else:
        print('false')    
    

func('hello harry')

func ('hello suraj')