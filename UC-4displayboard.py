#!/usr/bin/env python
# coding: utf-8

# UC-4:As a Player would like
# to see the board so I
# can choose the valid
# cells during my turn

# In[19]:

import os
import time

print("Play Tic tac Toe")
    
TTT = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1           
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
          
       


# In[ ]:




