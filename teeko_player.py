###############################################################################
## Semester:         CS 540 Spring 202
##
## This File:        teeko_player.py
## Author:           Andy O'Connell
## Email:            ajoconnell2@wisc.edu
## CS Login:         o-connell
##
###############################################################################
##                   fully acknowledge and credit all sources of help,
##                   other than Instructors and TAs.
##
## Persons:          N/A
##
## Online sources:   Lecture Notes and Piazza
##
###############################################################################

import random
from copy import deepcopy

class TeekoPlayer:
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    #Takes the board state and finds a list of legal successors
    def succ(self, state):
        element_count = 0
        for l in state:
            for elem in l:
                if (elem != ' '):
                    element_count+=1

        if (element_count < 8):
            drop = True  #detect drop phase
        else:
            drop = False

        successor_list = [] #row, col, number
        move_list = []
        succ_count = 0
        move_count = 0
        
        if not drop:
            for col in range(5):
                for row in range(5):
                    if (state[row][col] == self.my_piece):
                        if (row > 0):
                            if (state[row-1][col] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row-1][col] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row-1, col), (row, col)])
                                move_count += 1
                                succ_count+=1

                        if (row < 4):
                            if (state[row+1][col] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row+1][col] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row+1, col), (row, col)])
                                move_count += 1
                                succ_count+=1

                        if (col > 0):
                            if (state[row][col-1] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row][col-1] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row, col-1), (row, col)])
                                move_count += 1
                                succ_count+=1

                        if (col < 4):
                            if (state[row][col+1] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row][col+1] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row, col+1), (row, col)])
                                move_count += 1
                                succ_count+=1

                        if (row < 4 and col > 0):
                            if (state[row+1][col-1] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row+1][col-1] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row+1, col-1), (row, col)])
                                move_count += 1
                                succ_count+=1

                        if (row < 4 and col < 4):
                            if (state[row+1][col+1] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row+1][col+1] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row+1, col+1), (row, col)])
                                move_count += 1
                                succ_count+=1

                        if (row > 0 and col > 0):
                            if (state[row-1][col-1] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row-1][col-1] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row-1, col-1), (row, col)])
                                move_count += 1
                                succ_count+=1

                        if (row > 0 and col < 4):
                            if (state[row-1][col+1] == ' '):
                                copy_list = deepcopy(state)
                                copy_list[row-1][col+1] = state[row][col]
                                copy_list[row][col] = ' '
                                successor_list.append(copy_list)
                                move_list.append([(row-1, col+1), (row, col)])
                                move_count += 1
                                succ_count+=1
        elif (drop):
            for col in range(5):
                for row in range(5):
                    if (state[row][col] == ' '):
                        copy_list = deepcopy(state)
                        copy_list[row][col] = self.my_piece
                        successor_list.append(copy_list)
                        move_list.append([(row, col)])
                        move_count += 1
                        succ_count+=1
        returnDict = {"Succ": successor_list, "Moves": move_list}
        return returnDict
        
    #Starts with the current state of the board and generates a sub tree and uses a hueristic scoring function.
    #returns the best possible next move using minimax algorithm
    def make_move(self, state):
        element_count = 0
        for l in state:
            for elem in l:
                if (elem != ' '):
                    element_count+=1

        if (element_count < 8):
            drop = True  
        else:
            drop = False

        if not drop:
            move = []
            next_move = self.Max_Value(state, 0)[1]
            move.insert(0, next_move[1])
            move.insert(0, next_move[0])
            pass

        elif drop:
            move = []
            next_move = self.Max_Value(state, 0)[1]
            move.insert(0, next_move[0])
        
        return move

    #Makes the move of the opponent while checking if a piece is there and if it a illegal move at all
    def opponent_move(self, move):
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                raise Exception("You don't have a piece there!")

        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")

        self.place_piece(move, self.opp)
        
    #Places the piece
    def place_piece(self, move, piece):
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece
        
    #Prints the board
    def print_board(self):
        for row in range(len(self.board)):
            l = str(row)+": "
            for cell in self.board[row]:
                l += cell + " "
            
            print(l)
    
    
    #Heuristic algorithm that finds the best next move for the AI based on minimax algorithm
    def heuristic_game_value(self, state):
        if (self.game_value(state) != 0):
            return self.game_value(state)
        score1 = 0
        score2 = 0
        for col in range(5):
            for row in range(5):
                if (state[row][col] != ' '):
                        if (state[row][col] == self.my_piece):
                            if (row < 2):
                                for i in range(1,4):
                                    if (state[row+i][col] == state[row][col]):
                                        score1 += .25
                                
                            horazontal_score = 0
                            if (col < 2):
                                for i in range(1, 4):
                                    if (state[row][col+i] == state[row][col]):
                                        horazontal_score += .25
                                if (horazontal_score > score1):
                                    score1 = horazontal_score

                            diagonal_score = 0
                            if (col < 2 and row < 2):
                                for i in range(1, 4):
                                    if (state[row+i][col + i] == state[row][col]):
                                        diagonal_score += .25
                                if (diagonal_score > score1):
                                    score1 = diagonal_score

                            diagonal2_score = 0
                            if (col > 2 and row < 2):
                                for i in range(1,4):
                                    if state[row+i][col-i] == state[row][col]:
                                        diagonal2_score += .25
                                if (diagonal2_score > score1):
                                    score1 = diagonal2_score

                            box_score = 0
                            if (col < 4 and row < 4):
                                if (state[row + 1][col] == state[row][col]):
                                    box_score += .25
                                if (state[row][col+ 1] == state[row][col]):
                                    box_score += .25
                                if (state[row + 1][col + 1] == state[row][col]):
                                    box_score += .25
                                if (box_score > score1):
                                    score1 = box_score
                else:
                        if (row < 2):
                            for i in range(1,4):
                                if (state[row+i][col] == state[row][col]):
                                    score2 -= .25
                                
                            
                            horazontal_score = 0
                            if (col < 2):
                                for i in range(1, 4):
                                    if (state[row][col+i] == state[row][col]):
                                        horazontal_score -= .25
                                if (horazontal_score < score2):
                                    score2 = horazontal_score
                            
                            diagonal_score = 0
                            if (col < 2 and row < 2):
                                for i in range(1, 4):
                                    if (state[row+i][col + i] == state[row][col]):
                                        diagonal_score -= .25
                                if (diagonal_score < score2):
                                    score2 = diagonal_score
                            
                            diagonal2_score = 0
                            if (col > 2 and row < 2):
                                for i in range(1,4):
                                    if state[row+i][col-i] == state[row][col]:
                                        diagonal2_score -= .25
                                if (diagonal2_score < score2):
                                    score2 = diagonal2_score
                            
                            box_score = 0
                            if (col < 4 and row < 4):
                                if (state[row + 1][col] == state[row][col]):
                                    box_score -= .25
                                if (state[row][col+ 1] == state[row][col]):
                                    box_score -= .25
                                if (state[row + 1][col + 1] == state[row][col]):
                                    box_score -= .25
                                if (box_score < score2):
                                    score2 = box_score
        return score1
    
    #Finds the max value in the subtree
    def Max_Value(self, state, depth):
        if (depth >= 3 or self.game_value(state) != 0):
            return self.heuristic_game_value(state), [(0,0)]

        successor_list = self.succ(state)
        max_value = -1000
        i = 0
        max_index = 0

        for succ in successor_list["Succ"]:
            current_value = self.Min_Value(succ, depth + 1)[0]

            if (current_value > max_value):
                max_value = current_value
                max_index = i
            i+=1

        return max_value, successor_list["Moves"][max_index] #backpointers
        
    #Finds the min value in the algorithm
    def Min_Value(self, state, depth):
        if (depth >= 3 or self.heuristic_game_value(state) != 0):
            return self.heuristic_game_value(state), [(0,0)]
        
        successor_list = self.succ(state)
        minimum_value = 1000
        i = 0
        minimum_index = 0

        for succ in successor_list["Succ"]:
            current_value = self.Max_Value(succ, depth + 1)[0]
            if (current_value < minimum_value):
                minimum_value = current_value
                minimum_index = i
            i+=1

        return minimum_value, successor_list["Moves"][minimum_index]#backpointers(keeping track of min state)
        
    #Finds the score of each successor state
    def game_value(self, state):
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:

                    return 1 if row[i]==self.my_piece else -1

        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i+1][col] == state[i+2][col] == state[i+3][col]:

                    return 1 if state[i][col]==self.my_piece else -1
       
        for col in range(2):
            for row in range(2):
                    if (state[row][col] != ' ' and state[row][col] == state[row+1][col+1] == state[row+2][col+2] == state[row+3][col+3]):

                        return 1 if state[row][col]==self.my_piece else -1
       
        for col in range(3, 5):
            for row in range(2):
                    if (state[row][col] != ' ' and state[row][col] == state[row+1][col-1] == state[row+2][col-2] == state[row+3][col-3]):

                        return 1 if state[row][col]==self.my_piece else -1
  
        for col in range(4):
            for row in range(4):
                if (state[row][col] != ' ' and state[row][col] == state[row][col+1] == state[row+1][col] == state[row+1][col+1]):

                    return 1 if state[row][col]==self.my_piece else -1
        return 0 
        
