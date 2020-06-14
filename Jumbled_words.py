# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 08:54:14 2020
JUMBLED WORD
@author: Puruboi_Since_1998
"""
import random

def Choose():
    Words_Dict =['ability','about','administration','according','Flop','sack','duck','eat','water','rainbow', 'computer', 'science', 'programming', 
             'mathematics', 'player', 'condition', 'reverse', 
             'water', 'board', 'geeks' ]
    pick=random.choice(Words_Dict)
    return pick

def Jumble(word):
    jumbled= "".join(random.sample(word,len(word)))
    return jumbled

def Thank(pn1,pn2,pp1,pp2):
    print('{},your score is {}'.format(pn1,pp1))
    print('{},your score is {}'.format(pn2,pp2))
    
    if (pp1>pp2):
        print('{}, your the winner.'.format(pn1))
        
        print('Thanks for playing')
        print('Have a nice day')
        
    elif(pp2>pp1):
        print('{}, your the winner.'.format(pn2))
        
        print('Thanks for playing')
        print('Have a nice day')
     
    else:
        print ('Its a draw match')
        
        print('Thanks for playing')
        print('Have a nice day')
    
def Jumbled_words():
    # ask for their name 
    player_1 = input('player_1,please enter your name : ')

    player_2 = input('player_2,please enter your name : ')

    #initiailise the points
    player_1_points=0
    
    player_2_points=0
    
    #initialise the turn 
    turn=0 
    
    #game starts
    
    while(1):
        # computer task 
        picked_word = Choose()
        picked_word = picked_word.lower()
        #create question 
        q = Jumble(picked_word)
        print (q)
        
        # for player 1, turn is even 
        if (turn%2 == 0):
            print(player_1,'your turn ')
            
            a=(input('what is on your mind: '))
            a=a.lower()
            print(a)
            
            if (a is picked_word or a==picked_word ) :
                player_1_points=player_1_points+1
                print('your score is {}'.format(player_1_points))
                turn=turn+1
                
            else:
                print('the answer is wrong better luck next time') # chance to player 2                 print(player_2,'your turn ')
                a= input('what is on your mind: ')
                print(a)
                
                if (a==picked_word):
                    player_2_points+=1
                    print('your score is {}'.format(player_2_points))
                    
                else:
                    print('the answer is wrong better luck next time, the picked word is {}'.format(picked_word))
                    
                    # checking the c is equal to 0 or not 
                    # if c is equal to 0 then break out 
                    # of the while loop o/w keep looping
                    c=int(input('print 1 to continue and 0to quit'))
                    
                    if(c==0):
                        Thank(player_1,player_2,player_1_points,player_2_points)
                        break
                    
#for player 2 , turn is odd
                        
        else:
            print(player_2,'your turn ')
            a= input('what is on your mind: ')
            print(a)
            
            if (a==picked_word):
                player_2_points+=1
                print('your score is {}'.format(player_2_points))
                turn=turn+1
                
            else:
                print('the answer is wrong better luck next time')
                print(player_1,'your turn ')
                a=str(input('what is on your mind: '))
                print(a)
                
                if(a==picked_word):
                    player_1_points=player_1_points+1
                    print('your score is {}'.format(player_1_points))
                    
                else:
                    print('the answer is wrong better luck next time, the picked word is {}'.format(picked_word))
                    
                    c=int(input('print 1 to continue and 0to quit'))
                    
                    if(c==0):
                        Thank(player_1,player_2,player_1_points,player_2_points)
                        break
        c=int(input('print 1 to continue and 0to quit'))
        if(c==0):
            # calling thank you function 
            Thank(player_1,player_2,player_1_points,player_2_points)
            break        

Jumbled_words()
