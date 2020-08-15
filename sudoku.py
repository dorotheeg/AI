#!/usr/bin/env python
#coding:utf-8
import sys
import time
#   import numpy as np
from collections import Counter
from collections import defaultdict
import math
from statistics import stdev 

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):

    
    """Takes a board and returns solved board."""
    # TODO: implement this

    # get open locations
    #print(order_of_vars(board))
    
    # constraints
    # constraints(idx, value, board)

    #for each value in the ordered
    #try a value that is allowed
    #if it works add it and try to go on,
    #if you get to an impossible situation
    #go back and remove the last thing you did
    #do this until it works
    alls = (all_possible(board))
    sort = sorted(alls, key=lambda k: len(alls[k]), reverse=False)
    #got this here
    #https://stackoverflow.com/questions/16868457/python-sorting-dictionary-by-length-of-values

    if len(sort) == 0:
        print(time.time() - t1)
        return board
    
    idx = sort[0]
    #print(alls)
    #print(sort)
    #print("idx", idx)
    rang = alls[idx]
         
    for i in rang:
        #print("i", i)
        #print(idx)
        #rang.pop(0)
        if forward_checking(idx, i, board):
            board[idx] = i  
            if backtracking(board): # forward check, make sure it is allowed
                #print(t1- time.time())
                #print_board(board)
                return board
            board[idx] = 0

 
    return False
 

#def forward_checking(idx, value, board):

'''def back(order, board, alls):

    new_board = board
    
    if len(order) == 0:
        print(time.time() - t1)
        return board
    idx = order[0]
    #print("idx", idx)
    rang = alls[idx]
    
        
    for i in rang:
        if forward_checking(idx, i, board):
            new_board[idx] = i
            order.pop(0)
            if back(order, new_board, alls): # forward check, make sure it is allowed
                #print(t1- time.time())
                #print_board(board)
                return board
            order.insert(0,idx)
            new_board[idx] = 0
    
    return False'''

def forward_checking(idx, value, board):
    a = check_col(idx, value, board)
    b = check_row(idx, value, board)
    c = check_box(idx, value, board)

    if a == True and b == True and c == True:
        return True
    else:
        return False

def get_empty_locs(board):
    empty = []
    for i in board:
        if board[i] == 0:
            empty.append(i)
    return empty

def check_col(idx, value, board):
    col = idx[1]
    for i in board:
        if i[1] == col:
            if board[i] == value:
                return False
    return True

def check_row(idx, value, board):
    row = idx[0]
    for i in board:
        if i[0] == row:
            if board[i] == value:
                return False
    return True


def check_box(idx, value, board):

    row = idx[0]
    col = idx[1]
    sq,v = find_square(board, idx)
    for letter in sq:
        for val in v:
            if board[letter+val] == value:
                return False
    return True


def all_possible(board):
    t2 = time.time()
    my_dict = defaultdict(def_value)
    var = 0

    for x in get_empty_locs(board):
        my_dict[x] = []

    tots = [1,2,3,4,5,6,7,8,9]

    for each in my_dict.keys():
        for count in tots:
            
            if forward_checking(each, count, board):
                my_dict[each].append(count)
                var+=1
            else:
                var+=1
                
    return my_dict
    
    
'''
def row_val(i):
    pos = 0
    letters = ['x','A','B','C','D','E','F','G','H','I']
    if type(i) == int:
        return letters[i]
    else:
        for j in letters:
            if i == letters[pos]:
                return pos
            else:
                pos+=1'''

def find_square(board, idx):
    row = idx[0]
    col = idx[1]
    one = ['A', 'B', 'C']
    two = ['D', 'E', 'F']
    three = ['G', 'H', 'I']
    v1 = ['1', '2', '3']
    v2 = ['4', '5', '6']
    v3 = ['7', '8', '9']
    
    sq = []
    v = []

    if row in one:
        sq = one
    elif row in two:
        sq = two
    else:
        sq = three
        
    if int(col)  <=3:
        v = v1
    elif int(col) <=6:
        v = v2
    else:
        v = v3

    return sq, v

def def_value():
    pass

'''def order_of_vars(board):
    # check out of the empty which has most constraints, start with that one.
    free = get_empty_locs(board)
    #my_dict = defaultdict(def_value)
    
    
    my_dict = defaultdict(def_value)
    alph = ['A','B','C','D', 'E', 'F','G', 'H', 'I']
    
    for x in free:
        my_dict[x] = 0

    let = []
    num = []
    for each in board:
            let.append(each[0])
            num.append(each[1])
            
    
    for i in let:
        for j in range(10):
            var = str(i) + str(j)
            if var in my_dict:
                my_dict[var] +=1

    for i in alph:
        for j in num:
            var = str(i) + str(j)
            if var in my_dict:
                my_dict[var] +=1

    #print(my_dict)
    sort = sorted(my_dict, key=my_dict.get, reverse=True)
    # found this^^ here
    #https://stackoverflow.com/questions/20304824/sort-dict-by-highest-value             
    #print(sort)

    return sort
    #return free'''
         


if __name__ == '__main__':

    miny = 100
    maxy = -1
    mean = 0
    sd = 0
    total =0
    all_times = []
    
    if len(sys.argv) > 1:
        t1 = time.time()
        #  Read individual board from command line arg.
        sudoku = sys.argv[1]

        if len(sudoku) != 81:
            print("Error reading the sudoku string %s" % sys.argv[1])
        else:
            board = { ROW[r] + COL[c]: int(sudoku[9*r+c])
                      for r in range(9) for c in range(9)}
            
            print_board(board)

            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()

            print_board(solved_board)

            out_filename = 'output.txt'
            outfile = open(out_filename, "w")
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

    else:

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):
            t1 = time.time()

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                    for r in range(9) for c in range(9)}

            # Print starting board.
            print_board(board)

            # Solve with backtracking
            start_time = time.time()
            solved_board = backtracking(board)
            end_time = time.time()
            if (end_time - start_time) < miny:
                miny = end_time - start_time

            if (end_time - start_time) > maxy:
                maxy = end_time - start_time

            mean += end_time - start_time
            total +=1

            all_times.append(end_time - start_time)

            # Print solved board. 
            print_board(solved_board)
            

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

        print("Finishing all boards in file.")
        
        #print("MIN: ", miny)
        #print("MAX: ", maxy)
        #print("TOTAL SECONDS: ", mean)
        #print("MEAN: ", mean/total)
        #print("TOTAL SEEN: ", total)
        #print("STDEV: ", stdev(all_times))








