import sys
import os
import re
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


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
    print("#"+" "*13+"Press E for 10x10 game"+" "*13+"#")
    print("#"+" "*48+"#")
    print("#"+" "*14+"Press R for Controls"+" "*14+"#")
    print("#"+" "*48+"#")
    print("#"+" "*12+"Press T to quit the game"+" "*12+"#")
    for i in range(4):
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
            StartOfGameLoop(Board)
        elif(User_Input == 'w' or User_Input == 'W'): #starts a 5x5 game
            Board = CreatePlayingBoard(5)
            StartOfGameLoop(Board)
        elif(User_Input == 'e' or User_Input == 'E'): #starts a 10x10 game
            Board = CreatePlayingBoard(10)
            StartOfGameLoop(Board)
        elif(User_Input == 'r' or User_Input == 'R'): #displays the controls
            print("Showing off controls")
        elif(User_Input == 't' or User_Input == 'T'): #exits the program
            sys.exit()


"""Starts either a game for 2 players or a game against the AI"""
def StartOfGameLoop(Board):
    """Board: Array of arrays representing the playing board"""
    while True:
        ResetStartOfGameMenu()
        User_Input = input("Enter what you want to do: ")
        if(User_Input == 'q' or User_Input == 'Q'): #starts a game for 2 player
            print("Starting game for 2")
        elif(User_Input == 'w' or User_Input == 'W'): #starts a game against AI
            print("Starting game against AI")
        elif(User_Input == 'e' or User_Input == 'E'): #returns to menu
            return


"""Creates and returns an array of arrays that represents the playing board"""
def CreatePlayingBoard(size: int):
    """size: represents the size of the arrays SizexSize"""
    Board = []
    for r in range(size):
        Board.append([]) #each array represents a row
        for c in range(size):
            Board[r].append('.') #each . represents a square
    return Board


"""Takes input from the user and checks whether or not its a valid move"""
def PlayerInput(Board):
    """Board: Array of arrays that represents the playing board"""
    while True:
        inp = input("Make a move [X Y]: ") #takes input from the user
        if(re.match("(\d|10) (\d|10)", inp)): #checks if its in a correct format
            coordinates = [int(i) for i in inp.split()] #splits the input into coordinates
            if(coordinates[0] in range(1, len(Board) + 1) and coordinates[1] in range(1, len(Board) + 1)): #checks if the coordinates aren't out of bounds
                if(Board[coordinates[0] - 1][coordinates[1] - 1] == '.'): #checks if the tile isn't already filled
                    Board[coordinates[0] - 1][coordinates[1] - 1] = 'X' #fills the square
                    break



MenuLoop()