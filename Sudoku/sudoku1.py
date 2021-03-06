#Noah Hufnagel
#Sudoku Game, Text Based

import math
import numpy as np
import random

ROW=9
COL=9

puzzle= np.zeros((9,9))
path=[]
#print (puzzle)

def printPuzzle():
    rowCount=0
    for row in puzzle:
        colCount=0
        for num in row:
            colCount+=1
            print (f'{num:4g}', end='')
            if colCount%3==0 & colCount<9: print ('|', end='')
            if colCount==9: print()
        rowCount+=1
        if rowCount%3==0: print('_'*50) 
        else: print()


def solved():
    for row in puzzle:
        for num in row:
            if num==0: return False
    return True

def canBeAdded(x,y,num):
    #check to make sure each row is ok
    if num in puzzle[int(x)]: return False
    #check to make sure each collumn is ok
    for row in puzzle:
        if row[int(y)]==num: return False
    #check to make sure the 3x3 is ok
    left= math.floor(int(x)/3)
    top= math.floor(int(y)/3)
    for row in range(left,left+2):
        for col in range(top, top+2):
            if puzzle[row][col]==num: return False
    #else we return 1
    return True
            

def changeNum(x, y, num):
    if num != 0 & canBeAdded(x,y,num):
        puzzle[int(x)][int(y)]=int(num)
        #print(puzzle)
    
def generatePuzzle():
    SUDOKU_NUMBERS=[1,2,3,4,5,6,7,8,9]
    for i in range(0,81):
        # print(i)
        row=i//9
        col=i%9
        if puzzle[row][col]==0:
            random.shuffle(SUDOKU_NUMBERS)
            for number in SUDOKU_NUMBERS:
                if canBeAdded(row,col,number):
                    path.append((row,col,number))
                    changeNum(row,col,number)
                    if not solved():
                        return True
                    else:
                        if generatePuzzle():
                            return True
            break
    changeNum(row,col,0)
    return False


generatePuzzle()
printPuzzle()
# while  not solved():
#     printPuzzle()
#     print('add/change a number (x y number) or type stop to exit: ', end=' ')
#     recieved= input().split(' ')
#     if( len(recieved)==3): changeNum(recieved[0], recieved[1], recieved[2])
#     elif (recieved[0].lower()=="stop"): break
