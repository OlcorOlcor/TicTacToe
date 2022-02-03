from Menu import Menu
import os
import sys
import re
from AI import AI
from Board import Board

class Game():
    def __init__(self):
        self.Menu = Menu()
        self.Board = Board()
    
    """Starts a game in various modes, displays controls or exits the program based on user input"""
    def MenuLoop(self):
        while True:
            self.Menu.ResetMenu()
            User_Input = input("Enter what you want to do: ")
            if(User_Input == 'q' or User_Input == 'Q'): #starts a 3x3 game
                Board = self.Board.CreatePlayingBoard(3)
                self.StartOfGameLoop(Board, 3)
            elif(User_Input == 'w' or User_Input == 'W'): #starts a 5x5 game
                Board = self.Board.CreatePlayingBoard(5)
                self.StartOfGameLoop(Board, 4)
            elif(User_Input == 'e' or User_Input == 'E'): #starts a 9x9 game
                Board = self.Board.CreatePlayingBoard(9)
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
                self.PlayerInput(Board, "X's turn [X Y]: ", 'X')
                playing = False #switches the player
            else:
                self.PlayerInput(Board, "O's turn [X Y]: ", 'O')
                playing = True #switches the player
            result = self.Board.CheckWinningState(Board, Win_Condition)
            if(result is not None):
                self.ResetBoard(Board)
                if(result == 1):
                    print('X won')
                elif(result == -1):
                    print('O won')
                else:
                    print('Tie')
                input("Press Enter to return to Menu")
                return


    """Function for taking input for two player game"""
    def SinglePlayerGameLoop(self, Board, Win_Condition):
        """Board: Array of arrays representing the playing board
        Win_Condition: int representing how many symbols in a straight line it takes to win"""
        ai = AI(Win_Condition)
        playing = False #boolean representing which player is about to make a move (X/O)
        while True:
            self.ResetBoard(Board)
            if playing:
                self.PlayerInput(Board, "Player's turn [X Y]: ", 'O')
                playing = False #switches the player
            else:
                ai.CalculateMove(Board, 'X')
                playing = True #switches the player
            result = self.Board.CheckWinningState(Board, Win_Condition)
            if(result is not None):
                self.ResetBoard(Board)
                if(result == 1):
                    print('X won')
                else:
                    print('O won')
                input("Press Enter to return to Menu")
                return




    """Takes input from the user and checks whether or not its a valid move"""
    def PlayerInput(self, Board: list, Message: str, Symbol: str):
        """Board: Array of arrays that represents the playing board
        Message: Message that'll be written in input
        Symbol: Symbol that'll be added to the Board
        """
        while True:
            inp = input(Message) #takes input from the user
            if(re.match("(\d|10) (\d|10)", inp)): #checks if its in a correct format
                coordinates = [int(i) for i in inp.split()] #splits the input into coordinates
                if(coordinates[0] in range(1, len(Board) + 1) and coordinates[1] in range(1, len(Board) + 1)): #checks if the coordinates aren't out of bounds
                    if(Board[coordinates[0]][coordinates[1]] == '.'): #checks if the tile isn't already filled
                        Board[coordinates[0]][coordinates[1]] = Symbol #fills the square
                        return
            self.ResetBoard(Board)

