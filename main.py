import sys
import os


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
    print("#"+" "*12+"Press R to quit the game"+" "*12+"#")
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
            print("Playing 3x3 game")
        elif(User_Input == 'w' or User_Input == 'W'):
            print("Playing 5x5 game")
        elif(User_Input == 'e' or User_Input == 'E'):
            print("Playing 10x10 game")
        elif(User_Input == 'r' or User_Input == 'R'):
            sys.exit()
        else:
            ResetMenu()
        

DrawMenu()
MenuLoop()