def display(board):
    print('\n'*100)  #to scroll prev board out of view
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker=''
    while not(marker=='x' or marker=='o'):
        marker=input('player chose x or o')
    if marker=='x':
        return ('x','o')        
    else:
        return('o','x')    
import random
from turtle import position

def choosefirst():
    flip=random.randint(0,1)
    if flip==0:
        return 'player1'
    else:
        return 'player2' 

def place_marker(board,marker,position):
    return board[position]==marker
def space_check(board,position):
    return board[position]==' '


def win_check(board,mark):
    return((board[7]==board[8]==board[9]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[1]==board[2]==board[3]==mark) or
    (board[7]==board[5]==board[3]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[7]==board[4]==board[1]==mark) or
    (board[8]==board[5]==board[2]==mark) or
    (board[9]==board[6]==board[3]==mark) )

def playerchoice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose a position:1-9'))
        return position

print('welcome to tic tac toe')

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def replay():
    choice=input('play agaim? enter (yes or no') 
    return choice=='yes'           
            
while True:
    the_board=['']*10
    player1marker,player2marker=player_input()
    turn=choosefirst()
    print(turn+ 'will go first')
    playgame=input('ready to play?(y or n\n')
    if playgame=='y':
        game_on= True
    else:
        game_on=False
    while game_on:
        if turn=='player1'   :
            display(the_board)
            position=playerchoice(the_board)
            place_marker(the_board,player1marker)
            if win_check(the_board,player1marker):
                display(the_board)
                print('player1 has won!!')
                game_on=False
            else:
                if full_board_check(the_board) :
                    display(the_board)
                    print('tie game!')   
                    game_on=False
                else:
                    turn='player2'
        else:
            if turn=='player1'   :
                display(the_board)
                position=playerchoice(the_board)
                place_marker(the_board,player2marker)
                if win_check(the_board,player2marker):
                    display(the_board)
                    print('plater1 has won!!')
                    game_on=False
            else:
                if full_board_check(the_board) :
                    display(the_board)
                    print('tie game!')   
                    game_on=False
                else:
                    turn='player1'
    if not replay():
        break







