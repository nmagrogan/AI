'''
Class: CPSC 427 
Team Member 1: Nathan Magrogan
Team Member 2: Kaylee Moniz
Submitted By Nathan Magrogan
GU Username: nmagrogan
using python 3
File Name: proj6.py
Generates first-level child states from an initial state of the 8-puzzle, and then does a breadth
first search on the generated states to solve the 8puzzle
Reference: An Eight-Puzzle Solver in Python, https://gist.github.com/flatline/8382021
Usage: python proj6.py
'''

from copy import deepcopy

goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

class EightPuzzle:
    def __init__(self,parent):
        #state_lst now holds the root, the parent state
        self.state_lst = [[row for row in parent]]

    #displays all states in state_lst
    def display(self):
        for state in self.state_lst:
            for row in state:
                print(row)
            print ("")

    def display_state(self,state):
        for row in state:
            print(row)
        print ("")
        
    #returns (row,col) of value in state indexed by state_idx  
    def find_coord(self, value, state):
    
        for row in range(3):
            for col in range(3):
                if state[row][col] == value:
                    return (row,col)
        
                
    #returns list of (row, col) tuples which can be swapped for blank
    #these form the legal moves of the state indexed by state_idx
    def get_new_moves(self, state):
        row, col = self.find_coord(0,state) #get row, col of blank
        
        moves = []
        if col > 0:
            moves.append((row, col - 1))    #go left
        if row > 0:
            moves.append((row - 1, col))    #go up
        if row < 2:
            moves.append((row + 1, col))    #go down
        if col < 2:
            moves.append((row, col + 1))    #go right
        return moves

    #Generates all child states for the state indexed by state_idx
    #in state_lst.  Appends child states to the list
    def generate_states(self,state):
        
        #get legal moves
        move_lst = self.get_new_moves(state)

        newChildren = []
       
        #blank is a tuple, holding coordinates of the blank tile
        blank = self.find_coord(0,state)

        #tile is a tuple, holding coordinates of the tile to be swapped
        #with the blank
        for tile in move_lst:
            #create a new state using deep copy 
            #ensures that matrices are completely independent
            child = deepcopy(state)

            #move tile to position of the blank
            child[blank[0]][blank[1]] = child[tile[0]][tile[1]]

            #set tile position to 0                          
            child[tile[0]][tile[1]] = 0
            
            #append child state to the list of states.
            self.state_lst.append(child)
            newChildren.append(child)

        return newChildren

    def bredth_first(self):
        #def of varibles used by the search
        start = self.state_lst[0]
        open_lst = []
        closed = []
        open_lst.append(start)
        loop = 0
        
        

        while(open_lst):
            print("Iteration number: "+ str(loop))
            loop +=1
            cur = open_lst.pop(0)
            self.display_state(cur)
            if(cur == goal):
                return 1
            closed.append(cur)
            
            children = self.generate_states(cur)
            while(children):
                child = children.pop(0)
                if(child not in open_lst and child not in closed):
                    open_lst.append(child)
                   
        return 0
            

def main():
    #nested list representation of 8 puzzle. 0 is the blank.
    #This configuration is found on slide 8, E: Two Search Algorithms
    parent = [[2,8,3],
              [1,6,4],
              [7,0,5]]

    test = [[1,2,3],
            [8,0,4],
            [7,6,5]]
                   
    #initialize the list of states (state_lst) with the parent
    p = EightPuzzle(parent)

    print(p.bredth_first())
    
    
    
    #Generate the states reachable from the parent, i.e., 0th state in state_lst
    #p.generate_states(0)

    #display all states in state_lst                    
    #p.display()
    

main()

