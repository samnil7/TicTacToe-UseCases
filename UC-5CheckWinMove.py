#!/usr/bin/env python
# coding: utf-8

# UC-5:As player would expect
# the Tic Tac Toe App to
# determine after every
# move the winner or
# the tie or change the turn

# In[12]:


import os
import random
import time

print("Play Tic tac Toe")
    
TTT = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1   
  
Win = 1    
Draw = -1    
Running = 0    
Stop = 1       
Game = Running    
Mark = 'X'   

def DrawBoard():    
    print(" %c | %c | %c " % (TTT[1],TTT[2],TTT[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (TTT[4],TTT[5],TTT[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (TTT[7],TTT[8],TTT[9]))    
    print("   |   |   ")    
    
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(TTT[x] == ' '):    
        return True    
    else:    
        return False  
        
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(TTT[1] == TTT[2] and TTT[2] == TTT[3] and TTT[1] != ' '):    
        Game = Win    
    elif(TTT[4] == TTT[5] and TTT[5] == TTT[6] and TTT[4] != ' '):    
        Game = Win    
    elif(TTT[7] == TTT[8] and TTT[8] == TTT[9] and TTT[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(TTT[1] == TTT[4] and TTT[4] == TTT[7] and TTT[1] != ' '):    
        Game = Win    
    elif(TTT[2] == TTT[5] and TTT[5] == TTT[8] and TTT[2] != ' '):    
        Game = Win    
    elif(TTT[3] == TTT[6] and TTT[6] == TTT[9] and TTT[3] != ' '):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(TTT[1] == TTT[5] and TTT[5] == TTT[9] and TTT[5] != ' '):    
        Game = Win    
    elif(TTT[3] == TTT[5] and TTT[5] == TTT[7] and TTT[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(TTT[1]!=' ' and TTT[2]!=' ' and TTT[3]!=' ' and TTT[4]!=' ' and TTT[5]!=' ' and TTT[6]!=' ' and TTT[7]!=' ' and TTT[8]!=' ' and TTT[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running   
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
    
print("Please Wait...")    
time.sleep(3)    
while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPosition(choice)):    
        TTT[choice] = Mark    
        player+=1    
        CheckWin()    
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):    
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won")    


# In[ ]:




