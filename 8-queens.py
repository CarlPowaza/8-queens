
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
#------------------------genetic here--------------------------


def Average(lst):
    return sum(lst) / len(lst)

def intHelper(str):
    sub=re.split(' ',str)
    val =[]
    val.append(int(sub[0]))
    val.append(int(sub[1]))
    return val
def genetic():
    board = initPop()
    score = eval(board)
    sub = []
    temp =[]
  
    for i in range(1000):
        sub = intHelper(fitness(score))
        children = mating(board[sub[0]],board[sub[1]])
        temp = eval(children)
        if(Average(sub)>= Average(intHelper(fitness(temp)))):
            board = children
        score = eval(board)
      
        if(test(score)==0):
            return board[test(score)]
    return []
    
 
"""     for i in range(1000):
        sub = re.split(' ',fitness(score))
        temp = mating(board[int(sub[0])],board[int(sub[1])])
        board.append(temp[0])
        board.append(temp[1])
        score = eval(board)
      
        if(test(score)==0):
            return board[test(score)]
    return []       """  
        

#test if solution found
def test(score):
    for i in range(len(score)):
        if(score[i]==0):
            return  i

    return -1


    

def mating(p1,p2):# parent1 and 2
    children = []
    children.append(mutate([p1[0],p1[1],p1[2],p1[3],p2[4],p2[5],p2[6],p2[7]]))
    children.append(mutate([p2[0],p2[1],p2[2],p2[3],p1[4],p1[5],p1[6],p1[7]]))
    global cost
    cost+=2
    return children


def mutate(board):
    board[random.randrange(0,7)] = random.randrange(1,8)
    return board

def fitness(score):
    low =9001
    val1 =-1
    val2 =-1
    for i in range(len(score)):
        if(score[i] <=low):
            low = score[i]
            val2 =val1
            val1 =i
    return str(val1)+" "+str(val2)
            



def eval(board):
    values =[]
    for i in range(len(board)):
        values.append(heuristic(board[i]))
    return values



def initPop():
    board =[]
    for i in range(5):
        board.append(inititial_state())
    global cost
    cost+=5
    return board





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

    
    cost =0

    total =0
    solved =0  
    for i in range(input):
        if(len(genetic())>0):
            solved+=1
        
        total +=cost  
        cost =0
    total = total/input
    solved = (solved /input)*100
    print("Genetic:" +str(int(solved))+"% solved, average search cost:"+ str(int(total)))


main()
