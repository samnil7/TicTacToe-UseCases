#!/usr/bin/env python
# coding: utf-8

# UC-3:As a Player would like
# to begin with a toss to
# check who plays first.

# In[1]:
import os

print("Play Tic tac Toe")
    
TTT = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1      
Mark = 'X' 
Running = 0    
Stop = 1       
Game = Running  

while(Game == Running):    
   
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
            
    
os.system('cls')


# In[ ]:




