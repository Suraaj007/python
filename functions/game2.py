def display(game_list):
    print('here is your game list')
    print(game_list)


def position_choice():
    x='hjj'
    while x not in ['0','1','2']:
        x=input('enter a position u wana replace(0,1,2)\n')
        if x not in ['0','1','2'] :
            print('sorry invalid choice')
        else:
            pass
    return int(x)

def updatechoice(game_list,position):
    str1=input('enter a string\n')
    game_list[position]= str1
    return game_list

def  gameonchoice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input('keep playing?(y or n )')
        if choice not in ['y','n']:
            print('sorry invalid choice!!')
        if choice=="y":
            return True
        else:
            return False    
 

gameon= True
game_list=[0,1,2]

while gameon==True:
    display(game_list)
    position = position_choice()
    updatechoice(game_list,position)
    print(game_list)
    gameon=gameonchoice() 



 



