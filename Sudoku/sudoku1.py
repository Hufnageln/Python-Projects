#Noah Hufnagel
#Sudoku Game, Text Based

import math
import numpy as np

ROW=9
COL=9

puzzle= np.zeros((9,9))
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
            if num==0: return 0
    return 1

def canBeAdded(x,y,num):
    #check to make sure each row is ok
    if num in puzzle[int(x)]: return 0
    #check to make sure each collumn is ok
    for row in puzzle:
        if row[int(y)]==num: return 0
    #check to make sure the 3x3 is ok
    left= math.floor(int(x)/3)
    top= math.floor(int(y)/3)
    for row in range(left,left+2):
        for col in range(top, top+2):
            if puzzle[row][col]==num: return 0
    #else we return 1
    return 1
            

def changeNum(x, y, num):
    if num != 0 & canBeAdded(x,y,num):
        puzzle[int(x)][int(y)]=int(num)
        #print(puzzle)
    

while  not solved():
    printPuzzle()
    print('add/change a number (x y number): ', end=' ')
    recieved= input().split(' ')
    changeNum(recieved[0], recieved[1], recieved[2])
