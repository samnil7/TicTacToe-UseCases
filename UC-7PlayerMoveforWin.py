#!/usr/bin/env python
# coding: utf-8

# UC-6:On Computer getting 
# its turn would like the 
# computer to play like 
# me
# 
# UC-7:First thing I do is check 
# if I can win then play 
# that move

# In[3]:


import os
import time

print("Play Tic tac Toe")
    
TTT = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    

def DrawBoard():    
    print(" %c | %c | %c " % (TTT[1],TTT[2],TTT[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (TTT[4],TTT[5],TTT[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (TTT[7],TTT[8],TTT[9]))    
    print("   |   |   ")    

def insertBoard(letter, pos):
    global TTT
    TTT[pos] = letter
    
#This Function Checks position is empty or not    
def CheckPosition(pos):
    return TTT[pos] == ' '    
    
def isBoardFull(TTT):
    if TTT.count(' ') > 1:
        return False
    else:
        return True

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an X (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if CheckPosition(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
                                        
def CheckWin(bo, le):  
    
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the bottom
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the top
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal    
            
print("Player 1 [X] --- Player 2 [O]\n")    
print()        
print("Please Wait...")    
time.sleep(3)    
                  
def main():           
    DrawBoard()
    while not(isBoardFull(TTT)):
        if not(CheckWin(TTT, '0')):
            playerMove()
            DrawBoard()
        else:
            print('0 win this time..')
            break
  
    if isBoardFull(TTT):
        print('Game is a tie! No more spaces left to move')
main()



# In[ ]:




