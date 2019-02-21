'''
Class: CPSC 427 
Team Member 1: Nathan Magrogan
Team Member 2: Kaylee Moniz
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: proj5.py
Generates first-level child states from an initial state of the 8-puzzle
##Reference: An Eight-Puzzle Solver in Python, https://gist.github.com/flatline/8382021
Preforms a depth bound search on the states of the 8-puzzle to solve the puzzle
Usage: python proj5.py
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

    #displays one state
    def display_state(self,state):
        for row in state:
            print(row)
        print ("")
        
    #returns (row,col) of value in state  
    def find_coord(self, value, state):
    
        for row in range(3):
            for col in range(3):
                if state[row][col] == value:
                    return (row,col)
        
                
    #returns list of (row, col) tuples which can be swapped for blank
    #these form the legal moves of the state
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

    #Generates all child states for the state
    #Appends child states to the listl also returns a list of the generated states
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

    #preforms a depth first search with a depth bound to solve an 8 puzzle
    #given a starting state 
    def depth_first(self):
        #def of varibles used for the search algorithm
        start = self.state_lst[0]
        open_lst = []
        closed = []
        children = []
        state_level = [] #parrallel vector to open_list holds level int the graph of corresponding state in open_lst
        loop = 1
        DEPTH_BOUND = 5
        open_lst.append(start)
        state_level.append(0)
        
    
        while(open_lst):
            #displaying current state itteration number of algorithm and current level in graph
            loop += 1
            cur = open_lst.pop()
            cur_level = state_level.pop()
            print("Try number: " + str(loop))
            print("Level of graph: "+ str(cur_level))
            self.display_state(cur)

            #depth first algorithm
            if(cur == goal):
                return 1
            closed.append(cur)

            if(cur_level < DEPTH_BOUND):    #implementation of depth bound wont generate states bellow a certain level
                new_children = self.generate_states(cur)
                for new_child in new_children:
                    children.append(new_child)

            while(children):
                child = children.pop()
                if(child not in open_lst and child not in closed):
                    open_lst.append(child)
                    state_level.append(cur_level+1)
                   
        return 0
            

def main():
    #nested list representation of 8 puzzle. 0 is the blank.
    #This configuration is found on slide 8, E: Two Search Algorithms
    parent = [[2,8,3],
              [1,6,4],
              [7,0,5]]

                       
    #initialize the list of states (state_lst) with the parent
    p = EightPuzzle(parent)

    #preform depth first search on the puzzle
    print(p.depth_first())
    
    

    

main()

