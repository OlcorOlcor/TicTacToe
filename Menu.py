import os
"""Used for diplaying menu into the console"""
class Menu():

    """Displays the menu in console"""
    def DrawMenu(self):
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
    def DrawStartOfGameMenu(self):
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
    def ResetMenu(self):
        clear = lambda: os.system('cls')
        clear()
        self.DrawMenu()


    """Clears the console and calls DrawStartOfGameMenu function"""
    def ResetStartOfGameMenu(self):
        clear = lambda: os.system('cls')
        clear()
        self.DrawStartOfGameMenu()