# Bad implementation of a Pennet Square calculator.
# This WILL break if its not a double gene pennet square. A monohybrid is trivial to calculate anyways. 

# test commit
# This currently only outputs though using print statements.
# A migration to NumPY's Array system is currently being made. 
# Working towards an input system for alleles, as well as generalizing this to an n by n size allele hybrid is currently on the to-do list. 

import numpy as np  # type: ignore
#test
#Gene 1 Alleles. a,b -> AABB 
a =str(input("Input gene 1 allele 1:"))
b =str(input(("Input Gene 1 Alelle 2 (current gene: " + a + "XX): ")))
print("Gene 1: ",(a + b))
#Gene 2 Alleles. c,d -> CCDD
c =str(input("Input gene 2 allele 1:"))
d =str(input(("Input Gene 2 Alelle 2 (current gene: " + c + "XX): ")))
print("Gene 2: ",(c + d))
# First Letter
# set this as the letter of the first gene. 
first=a[0]

# Dom Fix: Append something to the front! 
# 01 -> 10
def Dom_fix(a):
    index = 0
    fixedletter = "" #takes in a string and appends capitals at the front 
    properstr = ""
    for i in a: 
        properstr = properstr + i
    if properstr.isupper() == True: 
        #print(a)
        return properstr
    for l in properstr: 
        if l.isupper() == True: # if the letter is uppercase 
            fixedletter = l + properstr[1-index] # append the other string
            return fixedletter
        else: #else 
            index = index + 1 
    return a 
        
        
# Basic implementation of the "FOIL" method.
# A -> (a,b)
# B -> (c,d)
# for every A, combine it with every B: ac, ad. Only then we iterate to bc and bd.          
def FOIL(a,b):
    to_output = [] #output list
    for i in a: # for every 
        for i_2 in b: 
            h = i + i_2
            to_output.append(Dom_fix(h))
    return to_output

def GLT (a): #Fixes letter arrangement, rather, arranges the genes together. 
    letter_1 = [] #First letter in arrangement. Depenent on "first" variable.
    letter_2 = [] #Second letter in arrangement. 
    
    for i in a: 
        if i.upper() == first.upper():
            letter_1.append(i)
        else: 
            letter_2.append(i)    
    letter_1 = Dom_fix(letter_1) 
    letter_2 = Dom_fix(letter_2)
    if len(a) == 2: #special case for 2 length characters, such as maybe our input arrays
        return letter_1[0] + letter_2[0]
    else:
        return letter_1[0] + letter_1[1] + letter_2[0] + letter_2[1] #Takes the first two letters of letter_1 then merges then with letter_2 in a str.

def pennet_square (A,B):  
    # define A as the top row, and B as the side column
    # for a 2x1 [ab] * 1x2 [cd] matrix, the resulting 2x2 matrix is: 
    # ac ad bc bd or 1,1 x 1,1  1,2 x 1.1 2,1 x 1
    # iterate Ys then X's 
    to_output = []
    top_display = []
    top_display_table = []
    ticker = 0
    side_display = []
    spacing = ""
    for i in B: 
        top_display_table.append((spacing + GLT(i)))
        top_display.append(GLT(i))
        spacing = spacing + " "
    for j in A: 
        side_display.append(GLT(j))
        

    print(a+b, " x ", c+d, "cross Via FOIL leads to:")
    print(side_display, " x ", top_display)
    print("---------------------")

    print(" X    ", top_display_table)
    for x in A:
       # print(x)
        to_output.append(GLT(x))
        ticker =+ 1 
        #print(b)
        for y in B:
            #print(x)
            to_output.append(GLT(y + x))

        print(to_output)
        to_output = []
    
#function proper         
pennet_square(FOIL(c,d),FOIL(a,b))

##print(FOIL(a,d))
#print(FOIL(b,c))
