from tokenize import cookie_re
from Menu import Menu
import os
import sys
import re
from AI import AI


class Game():
    def __init__(self):
        self.Menu = Menu()
    
    """Starts a game in various modes, displays controls or exits the program based on user input"""
    def MenuLoop(self):
        while True:
            self.Menu.ResetMenu()
            User_Input = input("Enter what you want to do: ")
            if(User_Input == 'q' or User_Input == 'Q'): #starts a 3x3 game
                Board = self.CreatePlayingBoard(3)
                self.StartOfGameLoop(Board, 3)
            elif(User_Input == 'w' or User_Input == 'W'): #starts a 5x5 game
                Board = self.CreatePlayingBoard(5)
                self.StartOfGameLoop(Board, 4)
            elif(User_Input == 'e' or User_Input == 'E'): #starts a 9x9 game
                Board = self.CreatePlayingBoard(9)
                self.StartOfGameLoop(Board, 5)
            elif(User_Input == 'r' or User_Input == 'R'): #displays the controls
                print("Showing off controls")
            elif(User_Input == 't' or User_Input == 'T'): #exits the program
                sys.exit()


    """Starts either a game for 2 players or a game against the AI"""
    def StartOfGameLoop(self, Board, Win_Condition):
        """Board: Array of arrays representing the playing board
        Win_Condition: int representing how many symbols in a straight line it takes to win
        """
        while True:
            self.Menu.ResetStartOfGameMenu()
            User_Input = input("Enter what you want to do: ")
            if(User_Input == 'q' or User_Input == 'Q'): #starts a game for 2 player
                self.TwoPlayerGameLoop(Board, Win_Condition)
                return
            elif(User_Input == 'w' or User_Input == 'W'): #starts a game against AI
                self.SinglePlayerGameLoop(Board, Win_Condition)
                return
            elif(User_Input == 'e' or User_Input == 'E'): #returns to menu
                return


    """Displays board in console"""
    def ResetBoard(self, Board):
        clear = lambda: os.system('cls')
        clear()
        for r in Board:
            print("".join(r))


    """Function for taking input for two player game"""
    def TwoPlayerGameLoop(self, Board, Win_Condition):
        """Board: Array of arrays representing the playing board
        Win_Condition: int representing how many symbols in a straight line it takes to win"""
        playing = True #boolean representing which player is about to make a move (X/O)
        while True:
            self.ResetBoard(Board)
            if playing:
                End = self.PlayerInput(Board, "X's turn [X Y]: ", 'X', Win_Condition)
                playing = False #switches the player
            else:
                End = self.PlayerInput(Board, "O's turn [X Y]: ", 'O', Win_Condition)
                playing = True #switches the player
            if End:
                return


    """Function for taking input for two player game"""
    def SinglePlayerGameLoop(self, Board, Win_Condition):
        """Board: Array of arrays representing the playing board
        Win_Condition: int representing how many symbols in a straight line it takes to win"""
        ai = AI(Win_Condition)
        playing = True #boolean representing which player is about to make a move (X/O)
        while True:
            self.ResetBoard(Board)
            if playing:
                End = self.PlayerInput(Board, "Player's turn [X Y]: ", 'X', Win_Condition)
                playing = False #switches the player
            else:
                ai.CalculateMove(Board, 'O')
                playing = True #switches the player
            if End:
                return

    """Creates and returns an array of arrays that represents the playing board"""
    def CreatePlayingBoard(self, size: int):
        """size: represents the size of the arrays SizexSize"""
        Board = []
        Board.append([])
        Board[0].append('#') #adds '#' to the top left corner of the playing board
        for c in range(1, size + 1): #adds the first row with column numbers
            Board[0].append(str(c))
        rowcount = 1
        for r in range(1, size + 1):
            Board.append([]) #each array represents a row
            Board[r].append(str(rowcount)) #adds row number at the start of row
            for c in range(size):
                Board[r].append('.') #each . represents a square
            rowcount += 1 
        return Board


    """Takes input from the user and checks whether or not its a valid move"""
    def PlayerInput(self, Board: list, Message: str, Symbol: str, Win_Condition: int):
        """Board: Array of arrays that represents the playing board
        Message: Message that'll be written in input
        Symbol: Symbol that'll be added to the Board
        Win_Condition: int representing how many symbols in a straight line it takes to win
        """
        while True:
            inp = input(Message) #takes input from the user
            if(re.match("(\d|10) (\d|10)", inp)): #checks if its in a correct format
                coordinates = [int(i) for i in inp.split()] #splits the input into coordinates
                if(coordinates[0] in range(1, len(Board) + 1) and coordinates[1] in range(1, len(Board) + 1)): #checks if the coordinates aren't out of bounds
                    if(Board[coordinates[0]][coordinates[1]] == '.'): #checks if the tile isn't already filled
                        Board[coordinates[0]][coordinates[1]] = Symbol #fills the square
                        if(self.CheckWinCondition(Board, coordinates, Symbol, Win_Condition)):
                            self.ResetBoard(Board)
                            print(Symbol + " won")
                            input("Press Enter to return to Menu")
                            return True
                        return False
            self.ResetBoard(Board)


    """Checks if board is in a winning state for one of the players"""
    def CheckWinCondition(self, Board: list, Coordinates: tuple, Symbol: str, Win_Condition: int):
        """Board: Array of arrays that represents the playing board
        Coordinates: Tuple that represents last move.
        Symbol: Represent players symbol (X/O)
        Win_Condition: int representing how many symbols in a straight line it takes to win
        """
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)] #directions that will be checked for win condition (right, left, up, down, top-right, bottom-left, bottom-right, top-left)
        
        for i in range(0, 7, 2 ): #4 cycles for every column, row and diagonal.
            if(Coordinates == [1, 3] and i == 6):
                print()
            count = 0
            count += self.SearchInADirection(Board, directions[i], Symbol, Coordinates[:])
            count += self.SearchInADirection(Board, directions[i + 1], Symbol, Coordinates[:])
            count -= 1 #1 is substracted because the symbol on starting coordinates is counted twice
            if(count >= Win_Condition):
                return True
        return False


    """Counts how many of the same symbol are in a straight line"""
    def SearchInADirection(self, Board: list, direction: tuple, Symbol: str, current_Coordinates: tuple):
        """Board: Array of arrays that represent the playing board
        direction: coordinates that are added/substracted from the position
        symbol: symbol to be checked
        current_coordinates: starting coordinates"""
        count = 0
        current = Board[current_Coordinates[0]][current_Coordinates[1]] #Symbol to be checked
        if current_Coordinates[0] + direction[0] >= len(Board) or current_Coordinates[1] + direction[1] >= len(Board): #adds one to the counter in the case of the symbol being right on the edge
            count += 1
            return count
        while current == Symbol: #Loops as long as current position still has the right symbol and the position isn't out of bounds.
            if(current_Coordinates[0] + direction[0] >= len(Board) or current_Coordinates[1] + direction[1] >= len(Board)):
                count += 1
                break
            count += 1
            current_Coordinates[0] += direction[0]
            current_Coordinates[1] += direction[1] 
            current = Board[current_Coordinates[0]][current_Coordinates[1]] #changes current symbol to the next square
        return count