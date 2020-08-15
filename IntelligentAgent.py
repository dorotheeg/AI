import random
from BaseAI import BaseAI
from statistics import mean
import time
import math
from copy import deepcopy



it = 0

class IntelligentAgent(BaseAI):
    def getMove(self, grid):
        t1 = time.clock()
        depth = 1
        moveset = grid.getAvailableMoves()
        maxUtil = -math.inf
        good_move = -math.inf
        
        #mini = maxy(grid, depth, t1, -999)
  
        for move in moveset:
            #print(move[0])
                
            
            child = poss_child(grid, move[0])

            #val  = decision(grid, depth, t1)
            val = decision(child, depth, t1)
            if 0 in move or 2 in move:
                
                val += 15
            #print(val)
            if val >= maxUtil:
                maxUtil = val
                good_move = move[0]
                
        return good_move


def not_leaf(grid):
    #returns true if it is not a leaf node
    return grid.canMove()


def poss_child(grid, move):
    #returns child if this move is possible
    temp = grid.clone()
    temp.move(move)
    return temp


def all_child(grid):
    children = []
    for move in grid.getAvailableMoves():
        kid = poss_child(grid, move)
        children.append(kid)
    return children


def maxy(grid, depth, t1, a, b):
    if not not_leaf or depth >=4 or (time.clock() - t1) > 0.1:
        #reurn heursitc of it
        return evalutate(grid)
    else:
        maxChild = None
        maxUtility = -math.inf

        sibs = all_child(grid)

        for child in sibs:
            util = miny(child, depth+1, t1,  a ,b)
            #print("util", util)
            maxUtility = max(maxUtility, util)
            maxChild = child

            if maxUtility >= b:
                break

            a = max(a, maxUtility)
        

        #print("max", maxUtility)
        #print("child", child.map)
        return maxUtility


def chance(grid):

        avail = grid.getAvailableCells()
        sibs = []

        for cell in avail:
            min_child_grid = grid.clone()
            min_child_grid.insertTile(cell, 2)
            sibs.append(min_child_grid)
        
        #print(meanUtility)
        return sibs

def miny(grid, depth, t1, a ,b ):
    if not not_leaf or depth >= 4 or (time.clock() -t1) > .1:
        #reurn heursitc of it
        #print(a)
        return evalutate(grid)
    else:
        #computer
        minChild = None
        minUtility = math.inf

        sibs = chance(grid)

        for child in sibs:
            util = maxy(child, depth+1, t1, a ,b)
            minUtility = min(minUtility, util)

            if minUtility <= a:
                break

            b = min(b, minUtility)
            
        return minUtility
            
            
def decision(grid, depth, t1):
    child = maxy(grid, depth, t1, -math.inf , math.inf)
    return child
        
            
'''
def Expectiminimax(grid, depth, t1):

    modes = [1,0,-1]
    val = -math.inf
    #1 is max, 0 is chance, -1 is min modes

    global it
    state = modes[it]

    if state > 0:
        val = maxy(grid, depth, t1, -math.inf , math.inf)

    elif state == 0:
        val = chance(grid, depth, t1, -math.inf , math.inf)

    else:
        val = miny(grid, depth, t1, -math.inf , math.inf)
        

    if it < 2:
        it+=1
    else:
        it = 0

    return val
'''

def evalutate(grid):
    #print(grid.map)
    #print(grid.getAvailableMoves())
    #print("UD - T", grid.moveUD(True))
    #print("RL - T",grid.moveLR(True))
#    val = smoothness(grid) + free_spaces(grid) + \
#          monotonicityLR(grid) + poss_mergers(grid) + \
#          weight(grid)
    #print(val)
    #print(weight(grid))
    # poss_mergers(grid) + free_spaces(grid)  512
    # weight(grid) 256
    # weight(grid) + poss_mergers(grid) + free_spaces(grid) 512
    # (weight(grid))  + free_spaces(grid) 1024
    #print(edge(grid))
    return (weight(grid))  + (5* free_spaces(grid)) #+ edge(grid)


def monotonicityLR(grid):

    temp1 = []
    alt = []
    
    for i in (grid.map):
        alt = [x for x in i if x != 0]

        if all(alt[j] >= alt[j+1] for j in range(len(alt)-1)) :
            temp1.append(20)
        else:
            temp1.append(-20)

    return min(temp1)


def monotonicityUD(grid):
    mono = 0
    temp = []
    temp1 = []
    t1 = 0
    t2 = 0
    alt = []
    
    board = grid.map
    j = 0

    for i in range(3):
        if board[j][i] >= board[j+1][i]:
            temp.append(10)
        else:
            temp.append(-10)
        if j < 2:
            j+=1
        else:
            j = 0
    #print(min(temp))
    return min(temp)
        

def smoothness(grid):

    smooth = 0
    temp = math.inf
    for i in (grid.map):
        temp = min((min(i) - max(i)), temp)

    smooth += temp

    return smooth
    

def free_spaces(grid):
    tots = 0
    avail = grid.getAvailableCells()
    tots = len(avail)

    return tots


def poss_mergers(grid):
    most = 0

    for move in grid.getAvailableMoves():
        test = grid.clone()
        test.move(move)
        most = max(most, free_spaces(test))
    #print(most)
    return most*2


def weight(grid):
    tots = 1
    
    wm = [[math.pow(4,16),math.pow(4,14), math.pow(4,13), math.pow(4,12) ], \
          [math.pow(4,8),math.pow(4,9), math.pow(4,10), math.pow(4,11) ], \
          [math.pow(4,7),math.pow(4,6), math.pow(4,5), math.pow(4,4) ], \
          [math.pow(4,0),math.pow(4,1), math.pow(4,2), math.pow(4,3) ]]

    for i in range(4):
        for j in range(4):
            
            tots += (wm[i][j] * grid.map[i][j])

    #print(tots)
    return tots #(math.log(tots))
    

def edge(grid):
    '''if grid.getMaxTile() == (grid.map [0][0]):
        return 2
    elif grid.getMaxTile() in (grid.map [0]):
        return 1'''
    return 0


'''
recursive, at every level you check the grid state
similar to dfs that you're doing one option at a time
minimax are alternating depths showing the computer's move and then the
players's move.

start with max, then you choose between the moves
the next tile that you are adding is the chance part
from max you have 4 diff children that represent diff moves, each of those is a chnace move

tricky part, savinf on space,

after you choose 2 or 4, what is the next layer?
once you know what the value is you place it on the board,

min layer is the computer adveserial part

try to draw the tree, creating recursive function

QUESTION: recurssive part?
The mean/chance part chance part?

.90*2 -> chance weighted avg of resulted min nodes

figure out how to wight them, which to focus on mostly, snake?

sample, score gets updated


'''

