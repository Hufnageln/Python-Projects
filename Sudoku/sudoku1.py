#from graphics import *
#window= GraphWin(width=1000, height=1000)

ROW=9
COL=9

puzzle= [[0]*ROW]*COL

def printPuzzle():
    rowCount=0
    for row in puzzle:
        colCount=0
        for num in row:
            colCount+=1
            print ('{:4}'.format(num), end='')
            if colCount%3==0 & colCount<9: print ('|', end='')
            if colCount==9: print()
        rowCount+=1
        if rowCount%3==0: print('_'*50) 
        else: print()


printPuzzle()