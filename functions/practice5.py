#Given a no. n, return true if max deviation is 10 on either side from 100 and 200
def func(a):

    if  a in range(190,211): 
        print('true')
    elif a in range(90,111):
        print('true')
    else:
        print('false')        

func(90)
func(105)
func(125)
func(210)