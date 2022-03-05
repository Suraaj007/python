from random import choice


def check():
    choice='hahah'
    acceptablerange= range(0,11)
    withinrange=False
    while withinrange==False:

        choice=input('enter a no. in digit\n')
        if choice.isdigit()== False:
            print('sorry that is not a digit!!!')
        if choice.isdigit()==True:
            if int(choice) in acceptablerange:
                withinrange=True
            else:
                print('digit entered not in range!!')    

    return int(choice)
check()        