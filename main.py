import sys
import os
import re

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


def ResetMenu():
    clear = lambda: os.system('cls')
    clear()
    DrawMenu()


def MenuLoop():
    while True:
        User_Input = input("Enter what you want to do: ")
        if(User_Input == 'q' or User_Input == 'Q'):
            Board = CreatePlayingBoard(3)
            PlayerInput(Board)
        elif(User_Input == 'w' or User_Input == 'W'):
            Board = CreatePlayingBoard(5)
        elif(User_Input == 'e' or User_Input == 'E'):
            Board = CreatePlayingBoard(10)
        elif(User_Input == 'r' or User_Input == 'R'):
            print("Showing off controls")
        elif(User_Input == 't' or User_Input == 'T'):
            sys.exit()
        else:
            ResetMenu()
        

def CreatePlayingBoard(size):
    Board = []
    for r in range(size):
        Board.append([])
        for c in range(size):
            Board[r].append('.')
    return Board


def PlayerInput(Board):
    while True:
        inp = input("Make a move [X Y]: ")
        if(re.match("(\d|10) (\d|10)", inp)):
            coordinates = [int(i) for i in inp.split()]
            if(coordinates[0] in range(1, 4) and coordinates[1] in range(1, 4)):
                if(Board[coordinates[0] - 1][coordinates[1] - 1] == '.'):
                    Board[coordinates[0] - 1][coordinates[1] - 1] = 'X'
                    break


DrawMenu()
MenuLoop()