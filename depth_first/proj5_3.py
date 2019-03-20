'''
Class: CPSC 427 
Team Member 1: Nathan Magrogan
Team Member 2: Kaylee Moniz
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: proj5.pyGenerates first-level child states from an initial state of the 8-puzzle
Reference: An Eight-Puzzle Solver in Python, https://gist.github.com/flatline/8382021
Usage: python proj5.py
'''

from copy import deepcopy

goal = [[1,2,3],
        [8,0,4],
        [7,6,5]]

class StateNode:
    def __init__(self,parent):
        self.state = [row for row in parent]
        self.level = 0


class EightPuzzle:
    def __init__(self,parent):
        #state_lst now holds the root, the parent state
        self.state_lst = [parent]

    #displays all states in state_lst
    def display(self):
        for state in self.state_lst:
            for row in state:
                print(row)
            print ("")

    #displays one state and its level
    def display_state(self,state_node):
        print (state_node.level)
        for row in state_node.state:
            print(row)
        print ("")
        
        
    #returns (row,col) of value in state indexed by state_idx  
    def find_coord(self, value, state_node):
        for row in range(3):
            for col in range(3):
                if state_node[row][col] == value:
                    return (row,col)
        
                
    #returns list of (row, col) tuples which can be swapped for blank
    #these form the legal moves of the state indexed by state_idx
    def get_new_moves(self, state_node):
        row, col = self.find_coord(0,state_node) #get row, col of blank
        
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
    def generate_states(self,state_node):
        
        
        #get legal moves
        move_lst = self.get_new_moves(state_node.state)

        newChildren = []
       
        #blank is a tuple, holding coordinates of the blank tile
        blank = self.find_coord(0,state_node.state)

        #tile is a tuple, holding coordinates of the tile to be swapped
        #with the blank
        for tile in move_lst:
            #create a new state using deep copy 
            #ensures that matrices are completely independent
            child = deepcopy(state_node)

            #move tile to position of the blank
            child.state[blank[0]][blank[1]] = child.state[tile[0]][tile[1]]

            #set tile position to 0                          
            child.state[tile[0]][tile[1]] = 0

            #change level
            child.level +=1
            
            #append child state to the list of states.
            self.state_lst.append(child)
            newChildren.append(child)

        return newChildren

    def depth_first(self):
        #def of varibles used by the search
        start = self.state_lst[0]
        open_lst = []
        closed = []
        children = []
        open_lst.append(start)

        

        while(open_lst):
            cur = open_lst.pop()
            self.display_state(cur)
            if(cur == goal):
                return 1
            closed.append(cur)

            if(cur.level <5):
                new_children = self.generate_states(cur)
                for new_child in new_children:
                    children.append(new_child)
            
                
            while(children):
                child = children.pop()
                if(child.state not in open_lst.state and child.state not in closed.state):
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

    start = StateNode(parent)
                   
    #initialize the list of states (state_lst) with the parent
    p = EightPuzzle(start)

    print(p.depth_first())
    
    
    
    #Generate the states reachable from the parent, i.e., 0th state in state_lst
    #p.generate_states(0)

    #display all states in state_lst                    
    #p.display()
    

main()

