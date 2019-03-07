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
        #state_lvl now hoilds level of the root (0)
        self.state_lvl = [0]

    #displays all states in state_lst
    def display(self):
        for state in self.state_lst:
            for row in state:
                print(row)
            print("")
        

    #displays a state referenced by state_idx
    def display_state(self, state_idx):
        print("Level in graph: "+ str(self.state_lvl[state_idx]))
        for row in self.state_lst[state_idx]:
            print(row)
        print("")
        
        
    #returns (row,col) of value in state indexed by state_idx  
    def find_coord(self, value, state_idx):
    
        for row in range(3):
            for col in range(3):
                if self.state_lst[state_idx][row][col] == value:
                    return (row,col)
        
                
    #returns list of (row, col) tuples which can be swapped for blank
    #these form the legal moves of the state indexed by state_idx
    def get_new_moves(self, state_idx):
        row, col = self.find_coord(0,state_idx) #get row, col of blank
        
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
    def generate_states(self,state_idx):
        
        #get legal moves
        move_lst = self.get_new_moves(state_idx)
       
        #blank is a tuple, holding coordinates of the blank tile
        blank = self.find_coord(0,state_idx)

        #tile is a tuple, holding coordinates of the tile to be swapped
        #with the blank
        for tile in move_lst:
            #create a new state using deep copy 
            #ensures that matrices are completely independent
            child = deepcopy(self.state_lst[state_idx])

            #move tile to position of the blank
            child[blank[0]][blank[1]] = child[tile[0]][tile[1]]

            #set tile position to 0                          
            child[tile[0]][tile[1]] = 0
            
            #append child state to the list of states.
            self.state_lst.append(child)
            self.state_lvl.append(self.state_lvl[state_idx]+1)

    #returns value of how "good" a certain state is
    def heuristic(self,state_idx):
        cost = 9 #9 = worst cost, all tiles in wrong place
        state = self.state_lst[state_idx]
        
        #how many of the tiles are in the right place
        for i in range(3):
            for j in range(3):
                if state[i][j] == goal[i][j]:
                    cost -= 1

        return cost
        


    def best_first(self):
        #def of varibles used by the search
        start = self.state_lst[0]
        open_lst = []
        open_index = []
        open_heuristic = []
        closed = []
        open_lst.append(start)
        open_index.append(0)
        open_heuristic.append(self.heuristic(0))
        loop = 0
        
        

        while(open_lst):
            print("Iteration number: "+ str(loop))
            loop +=1
            cur = open_lst.pop(0)
            cur_index = open_index.pop(0)
            cur_heuristic = open_heuristic.pop(0)
            
            self.display_state(cur_index)
            if(cur == goal):
                return 1

            lower_index = len(self.state_lst)
            self.generate_states(cur_index)
            upper_index = len(self.state_lst)

            
            for child_index  in range(lower_index,upper_index): #for each child of cs
                if(self.state_lst[child_index] not in open_lst or self.state_lst[child_index] not in closed):
                    child_heuristic = self.heuristic(child_index) + self.state_lvl[child_index]
                    open_lst.append(self.state_lst[child_index])
                    open_index.append(child)
                    open_heuristic.append(child_heuristic)

                elif self.state_lst[child] in open_lst:
                    old_index = open_lst.index(self.state_lst[child]) # correct???
                    depth_child = 
                    if g(child) < g(old_index)
                        g(child on open) = g(chid)
                elif self.state_lst[child] in closed:
                    print(3)
                    #if g(child)< g(child on closed)
                        #remove child from closed
                        #euque child;
            
                closed.append(self.state_lst[cur_index])
                #open sort

                 
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

    print(p.best_first())
    
    
    
    #Generate the states reachable from the parent, i.e., 0th state in state_lst
    #p.generate_states(0)

    #display all states in state_lst                    
    #p.display()
    

main()

