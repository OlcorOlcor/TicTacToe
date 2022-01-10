import sys
import os
import re


"""Displays the menu in console"""
def DrawMenu():
    print("#"*50)
    print("#"+" "*18+"TIC TAC TOE"+" "*19+"#")
    print("#"+" "*48+"#")
    print("#"+" "*22+"MENU"+" "*22+"#")
    for i in range(2):
        print("#"+" "*48+"#")
    print("#"+" "*14+"Press Q for 3x3 game"+" "*14+"#")
    print("#"+" "*48+"#")
    print("#"+" "*14+"Press W for 5x5 game"+" "*14+"#")
    print("#"+" "*48+"#")
    print("#"+" "*14+"Press E for 9x9 game"+" "*14+"#")
    print("#"+" "*48+"#")
    print("#"+" "*14+"Press R for Controls"+" "*14+"#")
    print("#"+" "*48+"#")
    print("#"+" "*12+"Press T to quit the game"+" "*12+"#")
    for i in range(2):
        print("#"+" "*48+"#")
    print("#"*50)


"""Displays the start of game menu in console"""
def DrawStartOfGameMenu():
    print("#"*50)
    print("#"+" "*48+"#")
    print("#"+" "*7+"Which mode would you like to play?"+" "*7+"#")
    print("#"+" "*48+"#")
    print("#"+" "*11+"Press Q for 2 player game"+" "*12+"#")
    print("#"+" "*48+"#")
    print("#"+" "*10+"Press W for game against AI"+" "*11+"#")
    print("#"+" "*48+"#")
    print("#"+" "*11+"Press E to return to menu"+" "*12+"#")
    print("#"+" "*48+"#")
    print("#"*50)


"""Clears the console and calls DrawMenu function"""
def ResetMenu():
    clear = lambda: os.system('cls')
    clear()
    DrawMenu()


"""Clears the console and calls DrawStartOfGameMenu function"""
def ResetStartOfGameMenu():
    clear = lambda: os.system('cls')
    clear()
    DrawStartOfGameMenu()


"""Starts a game in various modes, displays controls or exits the program based on user input"""
def MenuLoop():
    while True:
        ResetMenu()
        User_Input = input("Enter what you want to do: ")
        if(User_Input == 'q' or User_Input == 'Q'): #starts a 3x3 game
            Board = CreatePlayingBoard(3)
            StartOfGameLoop(Board, 3)
        elif(User_Input == 'w' or User_Input == 'W'): #starts a 5x5 game
            Board = CreatePlayingBoard(5)
            StartOfGameLoop(Board, 4)
        elif(User_Input == 'e' or User_Input == 'E'): #starts a 9x9 game
            Board = CreatePlayingBoard(9)
            StartOfGameLoop(Board, 5)
        elif(User_Input == 'r' or User_Input == 'R'): #displays the controls
            print("Showing off controls")
        elif(User_Input == 't' or User_Input == 'T'): #exits the program
            sys.exit()


"""Starts either a game for 2 players or a game against the AI"""
def StartOfGameLoop(Board, Win_Condition):
    """Board: Array of arrays representing the playing board
    Win_Condition: int representing how many symbols in a straight line it takes to win
    """
    while True:
        ResetStartOfGameMenu()
        User_Input = input("Enter what you want to do: ")
        if(User_Input == 'q' or User_Input == 'Q'): #starts a game for 2 player
            TwoPlayerGameLoop(Board, Win_Condition)
        elif(User_Input == 'w' or User_Input == 'W'): #starts a game against AI
            print("Starting game against AI")
        elif(User_Input == 'e' or User_Input == 'E'): #returns to menu
            return


"""Displays board in console"""
def ResetBoard(Board):
    clear = lambda: os.system('cls')
    clear()
    for r in Board:
        print("".join(r))


"""Function for taking input for two player game"""
def TwoPlayerGameLoop(Board, Win_Condition):
    """Board: Array of arrays representing the playing board
    Win_Condition: int representing how many symbols in a straight line it takes to win"""
    playing = True #boolean representing which player is about to make a move (X/O)
    while True:
        ResetBoard(Board)
        if playing:
            Board = PlayerInput(Board, "X's turn [X Y]: ", 'X', Win_Condition)
            playing = False #switches the player
        else:
            Board = PlayerInput(Board, "O's turn [X Y]: ", 'O', Win_Condition)
            playing = True #switches the player



"""Creates and returns an array of arrays that represents the playing board"""
def CreatePlayingBoard(size: int):
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
def PlayerInput(Board: list, Message: str, Symbol: str, Win_Condition: int):
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
                    if(CheckWinCondition(Board, coordinates, Symbol, Win_Condition)):
                        print(Symbol + "won")
                        input()
                    return Board
        ResetBoard(Board)

"""Checks if board is in a winning state for one of the players"""
def CheckWinCondition(Board: list, Coordinates: tuple, Symbol: str, Win_Condition: int):
    """Board: Array of arrays that represents the playing board
    Coordinates: Tuple that represents last move.
    Symbol: Represent players symbol (X/O)
    Win_Condition: int representing how many symbols in a straight line it takes to win
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1) ,(-1, 1), (1, -1)] #directions that will be checked for win condition (right, left, up, down, top-right, bottom-left, bottom-right, top-left)
    for i in range(0, 7, 2 ): #4 cycles for every column, row and diagonal.
        count = 0
        count += SearchInADirection(Board, directions[i], Symbol, Coordinates[:])
        count += SearchInADirection(Board, directions[i + 1], Symbol, Coordinates[:])
        count -= 1 #+1 for itself
        if(count >= Win_Condition):
            return True
    return False

"""Counts how many of the same symbol are in a straight line"""
def SearchInADirection(Board: list, direction: tuple, Symbol: str, current_Coordinates: tuple):
    """Board: Array of arrays that represent the playing board
    direction: coordinates that are added/substracted from the position
    symbol: symbol to be checked
    current_coordinates: starting coordinates"""
    count = 0
    current = Board[current_Coordinates[0]][current_Coordinates[1]] #Symbol to be checked
    if current_Coordinates[0] + direction[0] >= len(Board) or current_Coordinates[1] + direction[1] >= len(Board):
        count += 1
    while current == Symbol and current_Coordinates[0] + direction[0] < len(Board) and current_Coordinates[1] + direction[1] < len(Board):
        count += 1
        current_Coordinates[0] += direction[0]
        current_Coordinates[1] += direction[1]
        current = Board[current_Coordinates[0]][current_Coordinates[1]]
    return count
MenuLoop()


