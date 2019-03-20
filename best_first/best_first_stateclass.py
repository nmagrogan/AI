'''
Class: CPSC 427 
Team Member 1: Nathan Magrogan
Team Member 2: none
Submitted By Nathan Magrogan
GU Username: nmagrogan
using python 2.7
File Name: proj7.py

Generates first-level child states from an initial state of the 8-puzzle, and then does a best
first search on the generated states to solve the 8puzzle
heuristic used: number of pieces in the right place.
Reference: An Eight-Puzzle Solver in Python, https://gist.github.com/flatline/8382021
Usage: python proj7.py
'''

from copy import deepcopy


goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

#class for state nodes to hold heuristic value and level of node, and puzle state
class State:
    def __init__(self,parent):
        self.state = [row for row in parent]
        self.level = 0
        self.heuristic_value = self.heuristic()
        
    #returns value of how "good" a certain state is
    def heuristic(self):
        cost = 9 #9 = worst cost, all tiles in wrong place
           
        #how many of the tiles are in the right place
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == goal[i][j]:
                    cost -= 1
        return cost
    def get_value(self):
        return(self.level + self.heuristic_value)
        


class EightPuzzle:
    def __init__(self,parent):
        #state_lst now holds the root, the parent state
        self.state_lst = [parent]
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
        print("Level in graph: "+ str(self.state_lst[state_idx].level))
        for row in self.state_lst[state_idx].state:
            print(row)
        print("")
        
        
    #returns (row,col) of value in state indexed by state_idx  
    def find_coord(self, value, state_idx):
    
        for row in range(3):
            for col in range(3):
                if self.state_lst[state_idx].state[row][col] == value:
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

            #changes cilds levl
            child.level += 1

            #move tile to position of the blank
            child.state[blank[0]][blank[1]] = child.state[tile[0]][tile[1]]

            #set tile position to 0                          
            child.state[tile[0]][tile[1]] = 0

            #update childs heuristic value
            child.heuristic()
            
            #append child state to the list of states.
            self.state_lst.append(child)
            

    
        
    def best_first(self):
        #def of varibles used by the search
        open_lst = [] #holds indexes of nodes on open
        open_states = []
        closed = [] #holds closed state nodes
        value = self.state_lst[0].get_value()
        open_lst.append((value,0))
        open_states.append((value,self.state_lst[0].state))
        loop = 0
        
        

        while(open_lst):
            print("Iteration number: "+ str(loop))
            loop +=1
            cur = open_lst.pop(0)
            cur_state = open_states.pop(0)
            print(cur)
            
            self.display_state(cur[1])
            if(cur_state[1] == goal):
                return 1

            lower_index = len(self.state_lst)
            self.generate_states(cur[1])
            upper_index = len(self.state_lst)

            
            for child_index  in range(lower_index,upper_index): #for each child of cs
                if(self.state_lst[child_index] not in open_states or
                   self.state_lst[child_index] not in closed):
                    value = self.state_lst[child_index].get_value()
                    open_lst.append((value,child_index))
                    open_states.append((value,self.state_lst[child_index].state))
                    
                elif self.state_lst[child_index].state in open_states:
                    old_index = open_states.index(self.state_lst[child_index].state) # correct???
                    if self.state_lst[child_index].level < self.state_lst[old_index].level:
                        open_lst[old_index][0] = self.state_lst[child_index].get_value()
                        
                elif self.state_lst[child_index].state in closed:
                    old_index = closed.index(self.state_lst[child_index].state)
                    if self.state_lst[child_index].level < self.state_lst[old_index].level:
                        closed.pop(old_index)
                        value = self.state_lst[child_index].get_value()
                        open_lst.append((value,child_index))
                        open_states.append((value,self.state_lst[child_index].state))
            

                closed.append(self.state_lst[cur[1]].state)
                open_lst.sort()
                open_states.sort()
                

                 
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


    start_state = State(parent)
    
                   
    #initialize the list of states (state_lst) with the parent
    p = EightPuzzle(start_state)

    print(p.best_first())
    
    
    
    #Generate the states reachable from the parent, i.e., 0th state in state_lst
    #p.generate_states(0)

    #display all states in state_lst                    
    #p.display()
    

main()

