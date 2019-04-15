'''
Class: CPSC 427
Team Member 1: Nathan Magrogan
Team Member 2: none
Submitted By Nathan Magrogan
GU Username: nmagrogan
File Name: othello.py
code for an othello game, lets playes go back and fourth
making moves in othello
'''

#some constants
VALID_COLUMN = ["A","B","C","D","E","F","G","H"]
VALID_ROW = [1,2,3,4,5,6,7,8]


class Othello:
    #creates a starting board
    def __init__(self):
        self.board = [[" ","A","B","C","D","E","F","G","H"],
                      ["1","0","0","0","0","0","0","0","0"],
                      ["2","0","0","0","0","0","0","0","0"],
                      ["3","0","0","0","0","0","0","0","0"],
                      ["4","0","0","0","B","W","0","0","0"],
                      ["5","0","0","0","W","B","0","0","0"],
                      ["6","0","0","0","0","0","0","0","0"],
                      ["7","0","0","0","0","0","0","0","0"],
                      ["8","0","0","0","0","0","0","0","0"],]
        #score where 0 is score for black and 1 is score for white
        self.score = [2,2]

    #displays the board
    def display_board(self):
            for row in self.board:
                print(row)
            print("")

    #asks for user input for a new pos to place a tile
    def input_pos(self,player_name):
        letter_pos = raw_input(player_name + " input column letter: " )
        while letter_pos not in VALID_COLUMN:
            letter_pos = raw_input("Invald only letters A-H: ")

        number_pos = input(player_name + " input row number: ")
        while number_pos not in VALID_ROW:
            number_pos = input("Invald only numbers 1-8: ")

        return letter_pos, number_pos

    #returns all adjacent tiles given a positon
    def get_adj_tiles(self,letter_pos_int,number_pos):
        #letter_pos_int = VALID_COLUMN.index(letter_pos)+1
        adjacent_tiles = [self.board[number_pos+1][letter_pos_int], #below
                          self.board[number_pos-1][letter_pos_int], #above
                          self.board[number_pos][letter_pos_int+1], #right
                          self.board[number_pos][letter_pos_int-1]] #left
        return adjacent_tiles

    #probes in a give direction from a point returns index of furthest same tile, or -1 if no valid move
    def probe(self,letter_pos,number_pos,dir,player_name):
        if dir == 0: #other letter space is below probe down
            for i in range(8,number_pos,-1):
                if self.board[i][letter_pos] == player_name:
                    return (i-1,letter_pos)
            return -1
        elif dir == 1: #other letter aboce, probe up
            for i in range(1,number_pos,1):
                if self.board[i][letter_pos] == player_name:
                    return (i+1,letter_pos)
            return -1
        elif dir == 2: # other letter is right proble right
            for i in range(8,letter_pos,-1):
                if self.board[number_pos][i] == player_name:
                    return (number_pos,i-1)
            return -1
        elif dir == 3: #other letter is left, probe left
            for i in range(1,letter_pos,1):
                if self.board[number_pos][i] == player_name:
                    return (number_pos,i+1)
            return -1


    def generate_legal_moves(self,player_name):
        next_moves = []
        if player_name == "B":
            opposite_name = "W"
        else:
            opposite_name = "B"

        for i in range(8): #i number
            for j in range(8): #j #letter
                #if a point with the opposite tile, get its adjacent tiles
                if self.board[i+1][j+1] == opposite_name:
                    adjacent = self.get_adj_tiles(i+1,j+1)
                    for k in range(len(adjacent)):
                        #if the adjacent tile is a blank space, probe in opposite
                        #dir to see if you can place a tile there
                        if adjacent[k] == player_name:
                            new_index = self.probe(i+1,j+1,k,player_name)
                            print new_index
                            if new_index != -1:
                                if k == 0:
                                    next_moves.append((i,j+1))
                                if k == 1:
                                    next_moves.append((i+2,j+1))
                                if k == 2:
                                    next_moves.append((i+1,j))
                                if k == 3:
                                    next_moves.append((i+1,j+2))

        return next_moves

    #checks to see if a valid position was givent for a new tile placement
    #will request new input untill a valid position is given
    def check_pos(self,letter_pos,number_pos,player_name):
        letter_pos_int = VALID_COLUMN.index(letter_pos)+1
        #generate all of next possible moves, check if new move is one of them
        next_moves = self.generate_legal_moves(player_name)
        move = (letter_pos_int,number_pos)


        while move not in next_moves:
            print "Invalid move, try agian"
            letter_pos,number_pos = self.input_pos(player_name)
            letter_pos_int = VALID_COLUMN.index(letter_pos)+1
            move = (letter_pos_int,number_pos)
            print move
            print next_moves



        return letter_pos,number_pos

    #flips tiles based newest move
    def flip_tiles(self,letter_pos,number_pos,player_name):
        letter_pos_int = VALID_COLUMN.index(letter_pos)+1
        adjacent_tiles = self.get_adj_tiles(letter_pos_int,number_pos)

        if player_name == "B":
            opposite_name = "W"
        else:
            opposite_name = "B"
        print "------"
        print adjacent_tiles
        for i in range(len(adjacent_tiles)):
            if adjacent_tiles[i] == opposite_name:
                new_index = self.probe(letter_pos_int,number_pos,i,player_name)
                print new_index

        exit()


    #runs through a single turn for a player
    def player_turn(self,player_name):
        #initial input
        letter_pos, number_pos = self.input_pos(player_name)

        #checks if initial input was in a valid position, if not it wil
        #request a new input till a valid one is given
        letter_pos,number_pos = self.check_pos(letter_pos,number_pos,player_name)

        if player_name == "B":
            self.score[0] = self.score[0]+1
        else:
            self.score[1] = self.score[1]+1

        #flips whatever other tiles need to be flipped and changes score
        self.flip_tiles(letter_pos,number_pos,player_name)

        #puts tile on board
        self.board[number_pos][VALID_COLUMN.index(letter_pos)+1] = player_name



def main():

    game = Othello()
    game.display_board()
    game.player_turn("B")
    game.display_board()
    game.player_turn("W")
    game.display_board()



main()
