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
    def get_adj_tiles(self,letter_pos,number_pos):
        letter_pos_int = VALID_COLUMN.index(letter_pos)+1
        adjacent_tiles = [self.board[number_pos+1][letter_pos_int], #above
                          self.board[number_pos-1][letter_pos_int], #below
                          self.board[number_pos][letter_pos_int+1], #right
                          self.board[number_pos][letter_pos_int-1]] #left
        return adjacent_tiles


    def generate_legal_moves(self,letter_pos,number_pos,player_name):
        next_moves = [('E',3)]

        return next_moves

    #checks to see if a valid position was givent for a new tile placement
    #will request new input untill a valid position is given
    def check_pos(self,letter_pos,number_pos,player_name):
        #generate all of next possible moves, check if new move is one of them
        next_moves = self.generate_legal_moves(letter_pos,number_pos,player_name)
        move = (letter_pos_int,number_pos)
        while move not in next_moves:
            print "Invalid move, try agian"
            letter_pos,number_pos = self.input_pos(player_name)
            move = (letter_pos,number_pos)

        exit()


        return letter_pos,number_pos

    #flips tiles based newest move
    def flip_tiles(self,letter_pos,number_pos):
        print "flip"


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
        self.flip_tiles(letter_pos,number_pos)

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
