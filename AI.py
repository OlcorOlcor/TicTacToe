from Decision_Tree import Decision_Tree
from Decision_Tree import Node
from Game import Game
import copy
class AI:


    def __init__(self, tree):
        self.tree = tree


    def Build_Decision_Tree(self, Board, Symbol, Win_Condition, root):
        for r in range(1, len(Board)): #rows
            for c in range(1, len(Board)): #colums
                if Board[r][c] == '.':
                    self.MakeMove(Board, r, c, Symbol, Win_Condition)
                    root.Add_A_Child(Node(root, r, c))
                    if Symbol == 'X':
                        self.Build_Decision_Tree(copy.deepcopy(Board), 'O', Win_Condition, root.children[-1])
                    else:
                        self.Build_Decision_Tree(copy.deepcopy(Board), 'X', Win_Condition, root.children[-1])



    def MakeMove(self, Board: list, x: int, y: int, Symbol: str, Win_Condition: int):
        """Board: Array of arrays that represents the playing board
        x: x coordinate
        y: y coordinate
        Symbol: Symbol that'll be added to the Board
        Win_Condition: int representing how many symbols in a straight line it takes to win
        """
        Board[x][y] = Symbol #fills the square
        if(self.CheckWinCondition(Board, [x, y], Symbol, Win_Condition)):
            return True
        return False

    """Checks if board is in a winning state for one of the players"""
    def CheckWinCondition(self, Board: list, Coordinates: tuple, Symbol: str, Win_Condition: int):
        """Board: Array of arrays that represents the playing board
        Coordinates: Tuple that represents last move.
        Symbol: Represent players symbol (X/O)
        Win_Condition: int representing how many symbols in a straight line it takes to win
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1) ,(-1, 1), (1, -1)] #directions that will be checked for win condition (right, left, up, down, top-right, bottom-left, bottom-right, top-left)
        for i in range(0, 7, 2 ): #4 cycles for every column, row and diagonal.
            count = 0
            count += self.SearchInADirection(Board, directions[i], Symbol, Coordinates[:])
            count += self.SearchInADirection(Board, directions[i + 1], Symbol, Coordinates[:])
            count -= 1 #1 is substracted because the symbol on starting coordinates is counted twice
            if(count >= Win_Condition):
                return True
        return False
    def SearchInADirection(self, Board: list, direction: tuple, Symbol: str, current_Coordinates: tuple):
        """Board: Array of arrays that represent the playing board
        direction: coordinates that are added/substracted from the position
        symbol: symbol to be checked
        current_coordinates: starting coordinates"""
        count = 0
        current = Board[current_Coordinates[0]][current_Coordinates[1]] #Symbol to be checked
        if current_Coordinates[0] + direction[0] >= len(Board) or current_Coordinates[1] + direction[1] >= len(Board): #adds one to the counter in the case of the symbol being right on the edge
            count += 1
        while current == Symbol and current_Coordinates[0] + direction[0] < len(Board) and current_Coordinates[1] + direction[1] < len(Board): #Loops as long as current position still has the right symbol and the position isn't out of bounds.
            count += 1
            current_Coordinates[0] += direction[0] 
            current_Coordinates[1] += direction[1] 
            current = Board[current_Coordinates[0]][current_Coordinates[1]] #changes current symbol to the next square
        return count