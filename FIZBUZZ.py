# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 08:09:07 2020
FIZBUZZ GAME 
@author: Puruboi_Since_1998

"""
def FIZBUZZ(r):
    #i=1
    # while start<=r: or 
    
    for i in range (1,r):
        if (i%3 == 0 and i%5 == 0):
            print(str(i)+'='+'FIZBUZZ')
        
        else:
            if(i%3 == 0):
                print(str(i)+' = FIZ')
        
            else:
                if (i%5 == 0):
                    print(str(i)+' = BUZZ')
        
                else:
                    print(i)
        
        i+=1


r = int(input('game starts with 1 , enter the end range = '))        
FIZBUZZ(r)