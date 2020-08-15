
from __future__ import division
from __future__ import print_function

import sys
import math
import time
import queue as Q
import resource
import numpy as np
import heapq


#### SKELETON CODE ####
## The Class that Represents the Puzzle
class PuzzleState(object):
    """
        The PuzzleState stores a board configuration and implements
        movement instructions to generate valid children.
    """
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        """
        :param config->List : Represents the n*n board, for e.g. [0,1,2,3,4,5,6,7,8] represents the goal state.
        :param n->int : Size of the board
        :param parent->PuzzleState
        :param action->string
        :param cost->int
        """
        if n*n != len(config) or n < 2:
            raise Exception("The length of config is not correct!")
        if set(config) != set(range(n*n)):
            raise Exception("Config contains invalid/duplicate entries : ", config)

        self.n        = n
        self.cost     = cost
        self.parent   = parent
        self.action   = action
        self.config   = config
        self.children = []

        # Get the index and (row, col) of empty block
        self.blank_index = self.config.index(0)

        #self.display() # I PUT THIS

    def display(self):
        """ Display this Puzzle state as a n*n board """
        for i in range(self.n):
            print(self.config[3*i : 3*(i+1)])

    def move_up(self):
        """ 
        Moves the blank tile one row up.
        :return a PuzzleState with the new configuration
        """
        #print("MOVE UP")

        #print(self.config[:3])
        if 0 in self.config[:3]:
            #print("Action not possible")
            return None
            
        else:
            index = self.config.index(0)
            new_index = index-3
            val = self.config[new_index]
            new_board = list(self.config)
            #print(val)
            #print(new_index)
            new_board[new_index] = 0
            new_board[index] = val
              
        #self.display()
        child = PuzzleState(new_board, self.n, parent = self, action = "Up", cost = self.cost+1)
        return child

        
        
      
    def move_down(self):
        """
        Moves the blank tile one row down.
        :return a PuzzleState with the new configuration
        """
        
        #print("MOVE Down")

        #print(self.config[-3:])
        if 0 in self.config[-3:]:
            #print("Action not possible")
            return None
            
        else:
            index = self.config.index(0)
            new_index = index+3
            val = self.config[new_index]
            new_board = list(self.config)
            new_board[new_index] = 0
            new_board[index] = val
            
             
        #self.display()
        #print(self.config)
        #print(new_board)
        child = PuzzleState(new_board, self.n, parent = self, action = "Down", cost = self.cost+1)
        return child
        

        #pass
        #return (PuzzleState(new_board, self.n, parent = self, action = "Down", cost = self.cost+1))
      
    def move_left(self):
        """
        Moves the blank tile one column to the left.
        :return a PuzzleState with the new configuration
        """

        #print("MOVE Left")

        if self.config.index(0) == 0 or self.config.index(0) == 3 or self.config.index(0) == 6:
            #print("Action not possible")
            return None
            
        else:
            index = self.config.index(0)
            new_index = index-1
            val = self.config[new_index]
            new_board = list(self.config)
            new_board[new_index] = 0
            new_board[index] = val

        child = PuzzleState(new_board, self.n, parent = self, action = "Left", cost = self.cost+1)
        return child

        
        #return (PuzzleState(new_board, self.n, parent = self, action = "Left", cost = self.cost+1))

    def move_right(self):
        """
        Moves the blank tile one column to the right.
        :return a PuzzleState with the new configuration
        """

        #print("MOVE Right")
        #print(self.config.index(0))

        if self.config.index(0) == 2 or self.config.index(0) == 5 or self.config.index(0) == 8:
            #print("Action not possible")
            return None
            
        else:
            index = self.config.index(0)
            new_index = index+1
            val = self.config[new_index]
            new_board = list(self.config)
            new_board[new_index] = 0
            new_board[index] = val
            
        child = PuzzleState(new_board, self.n, parent = self, action = "Right", cost = self.cost+1)

        return child

      
    def expand(self):
        """ Generate the child nodes of this node """
        
        # Node has already been expanded
        if len(self.children) != 0:
            return self.children
        
        # Add child nodes in order of UDLR
        children = [
            self.move_up(),
            self.move_down(),
            self.move_left(),
            self.move_right()]

        # Compose self.children of all non-None children states
        self.children = [state for state in children if state is not None]
        return self.children

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters
def writeOutput(path, cost, expanded, maxy, time, mem):
    ### Student Code Goes here
    print("path to goal:", path)
    print("cost of path:", cost)
    print("nodes expanded:", expanded)
    print("search depth:", cost)
    print("max search depth:", maxy)
    print("running time:", time)
    print("max ram usage:", mem/100000000.0)
    '''
    path to goal: [`Up', `Left', `Left']
    cost of path: 3
    nodes expanded: 10
    search depth: 3
    max search depth: 4
    running time: 0.00188088
    max ram usage: 0.07812500'''
    pass

def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###'
    t0 = time.time() #https://docs.python.org/3/library/time.html looked this up
    maxy = -1
    
    frontier = Q.Queue()
    #https://docs.python.org/3/library/queue.html
    
    frontier.put(initial_state)
    explored = set()
    
    ex = 0
    bool = True
    test = set()
    test.add(initial_state)
    #print(frontier)

    while not frontier.empty():
        
        #print(frontier.get())
        state = frontier.get()
        #print(state.display())
        
            
        if test_goal(state):
            temp = state
            path = []
            path.append(state.action)

            while temp.parent:
                path.insert(0,temp.parent.action)
                temp = temp.parent
            path = path[1:]
            cost = len(path)
            t1 = time.time()
            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            #looked the memory part up
            return writeOutput(path, cost, ex, maxy, t1-t0, mem)                 
        #if bool == True or state.config != initial_state.config:
        
    
        explored.add(tuple(state.config))
        neighbors = state.expand()
        ex+=1

        #test = set()
        #for each in frontier.queue:
        #    test.add(tuple(each.config))
            
        for neighbor in neighbors:
            #print(neighbor.config)      
            if tuple(neighbor.config) not in test:
                frontier.put(neighbor)
                test.add(tuple(neighbor.config))
                #front.append(neighbor)
    
                maxy = max(maxy, neighbor.cost)
                
                    
                
    return False


def dfs_search(initial_state):
    """DFS search"""
    ### STUDENT CODE GOES HERE ###

    t0 = time.time()
    maxy = -1
    
    frontier = set()
    explored = set()
    
    frontier.add(initial_state)
    test = set()
    test.add(initial_state)
    
    
    while len(frontier):
        state = frontier.pop()
        

        if test_goal(state):
            temp = state
            path = []
            path.append(state.action)
            while temp.parent:
                path.insert(0,temp.parent.action)
                temp = temp.parent
            path = path[1:]
            cost = len(path)
            t1 = time.time()
            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            return writeOutput(path, cost, len(explored), maxy, t1-t0, mem)     
            
        explored.add(tuple(state.config))
        neighbors = reversed(state.expand())

        
        for neighbor in neighbors:
            if tuple(neighbor.config) not in test:
                maxy = max(maxy, neighbor.cost)
                frontier.add(neighbor)
                test.add(tuple(neighbor.config))
                #front.append(neighbor)
                
                    
                

   
def A_star_search(initial_state):
    """A * search"""
    ### STUDENT CODE GOES HERE ###

    #print(calculate_total_cost(initial_state))

    t0 = time.time()
    maxy = -1
    
    frontier = list()
    explored = set()
    
    frontier.append((0, initial_state))
    test = set()
    test.add(initial_state)

    

    while len(frontier):
        state = frontier.pop(0)[1]
        #print(state.config)

        if test_goal(state):
            temp = state
            path = []
            path.append(state.action)
            while temp.parent:
                path.insert(0,temp.parent.action)
                temp = temp.parent
            path = path[1:]
            cost = len(path)
            t1 = time.time()
            mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss 
            return writeOutput(path, cost, len(explored), maxy, t1-t0, mem)     
            
        explored.add(tuple(state.config))
        #print(len(explored))
        neighbors = (state.expand())

                
        for neighbor in neighbors:
            if tuple(neighbor.config) not in test:
                maxy = max(maxy, neighbor.cost)
                dist = (calculate_total_cost(neighbor))
                frontier.append((dist, neighbor))
                frontier.sort(key = lambda x: x[0])
                test.add(tuple(neighbor.config))
                #front.append(neighbor)
                
    
    
    pass

    

def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""
    ### STUDENT CODE GOES HERE ###

    goal = [0,1,2,3,4,5,6,7,8]
    actual = state.config
    
    g2 = np.array(goal).reshape(3,3)
    a2 = np.array(actual).reshape(3,3)
    
    cost = calculate_manhattan_dist(g2, a2, 0) + state.cost
    return cost


def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    ### STUDENT CODE GOES HERE ###
    tots = 0
    g2 = idx
    a2 = value

    for i in range(1, 9):
        x,y = (np.where(a2 == i))
        x_goal, y_goal = (np.where(g2 == i))
        tots += (abs(x[0]-x_goal[0])+ abs(y[0]-y_goal[0]))
              
    return tots

def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    ### STUDENT CODE GOES HERE ###

    goal = [0,1,2,3,4,5,6,7,8]
    if goal == puzzle_state.config:
        return True
    else:
        return False

# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    search_mode = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = list(map(int, begin_state))
    board_size  = int(math.sqrt(len(begin_state)))
    hard_state  = PuzzleState(begin_state, board_size)
    start_time  = time.time()
    
    if   search_mode == "bfs": bfs_search(hard_state)
    elif search_mode == "dfs": dfs_search(hard_state)
    elif search_mode == "ast": A_star_search(hard_state)
    else: 
        print("Enter valid command arguments !")
        
    end_time = time.time()
    print("Program completed in %.3f second(s)"%(end_time-start_time))
    

if __name__ == '__main__':
    main()
    
