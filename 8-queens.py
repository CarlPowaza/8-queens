
#!/usr/bin/env python2
# # -*- coding: utf-8 -*-
""" 8-queens """
__author__ ="carl Powaza"
import random
import re
import sys


def costing(int):
    return

def hill_climbing():
    current =inititial_state()
    while True:
        neighbor = successor(current)
        if(heuristic(neighbor)>=heuristic(current)):
            return current
        current = neighbor

def inititial_state():
    #generate a new board,random
    board = [1,2,3,4,5,6,7,8]
    random.shuffle(board)
    return board

def successor(current):
    explored =0
    minVal =9001
    min_board =current
    for col in range(8):

        oldVal = current[col]

        for row in range(1,9):
            #print(str(explored))
            explored=explored+1
            board = current
            board[col]=row
            h= heuristic(board)
           # print(board)

            if(h < minVal):
                minVal = h
                min_board = board            
        current[col] = oldVal
        global cost
        cost = cost + explored
    return min_board

def horizontalAttacks(board):
    count=0
    for row in range(0,8):
        for q in range(0,8):
            if(row != q):
                if(board[row]==board[q]):
                   
                    count =count +1
    return count


def heuristic(board):
    return horizontalAttacks(board) +diagonalAttacks(board)

def diagonalAttacks(board):
    counter = 0
    for i, bp in enumerate(board):
        for j in range(i+1,len(board)):
            counter+= 1 if isInDiagonal(i,bp,j,board[j])else 0
        return counter

def isInDiagonal(i,q1,j,q2):
    den = float(q1-q2)
    return abs(q1-q2)==abs(i-j)

def isSolved(board):
    if(heuristic(board)==0):
        return True
    return False




cost =0
input = int(re.sub('[^0-9]+', '', sys.argv[1]))





def main():
    total =0
    solved =0
    for i in range(input):
      
        if(isSolved(hill_climbing())):
            solved +=1
        global cost
        total +=cost  
        cost =0

    total = total/input
    solved = (solved /input)*100
    print("Hill-climbing:" +str(int(solved))+"% solved, average search cost:"+ str(int(total)))


main()
