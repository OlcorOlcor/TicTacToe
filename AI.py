from Decision_Tree import Decision_Tree
from Decision_Tree import Node

class AI:


    def __init__(self, Win_Condition):
        self.Win_Condition = Win_Condition
        self.NumberOfMoves = 1 #start at 1 because the player always goes first


    def CalculateMove(self, Board, Symbol):
        bestScore = 100
        for r in range(1, len(Board)):
            for c in range(1, len(Board)):
                if(Board[r][c] == '.'):
                    self.NumberOfMoves += 1
                    Board[r][c] = Symbol
                    score = self.minimax(Board, True, 'X', r, c)
                    Board[r][c] = '.'
                    if(score < bestScore):
                        bestScore = score
                        bestMove = (r, c)
        Board[bestMove[0]][bestMove[1]] = Symbol
    
    
    def minimax(self, Board, isMax, Symbol, x, y):
        result = self.CheckWinCondition(Board, (x,y), Symbol)
        if(result == False and self.NumberOfMoves == (len(Board) - 1) * (len(Board) - 1)): #checks if the game state is a Tie
            return 0
        if(result): #checks if the game is in a winning state
            if(Symbol == 'X'): #returns 1 if X won
                return -1
            else: #returns -1 if O won
                return 1
        
        if (isMax):
            bestScore = -100
            for r in range(1, len(Board)):
                for c in range(1, len(Board)):
                    if(Board[r][c] == '.'):
                        self.NumberOfMoves += 1
                        Board[r][c] = Symbol
                        score = self.minimax(Board, False, 'O', r, c)
                        Board[r][c] = '.'
                        bestScore = max(score, bestScore)
        else:
            bestScore = 100
            for r in range(1, len(Board)):
                for c in range(1, len(Board)):
                    if(Board[r][c] == '.'):
                        self.NumberOfMoves += 1
                        Board[r][c] = Symbol
                        score = self.minimax(Board, True, 'X', r, c)
                        Board[r][c] = '.'
                        bestScore = min(score, bestScore)
        return bestScore

    def MakeMove(self, Board: list, x: int, y: int, Symbol: str, Win_Condition: int):
        """Board: Array of arrays that represents the playing board
        x: x coordinate
        y: y coordinate
        Symbol: Symbol that'll be added to the Board
        Win_Condition: int representing how many symbols in a straight line it takes to win
        """
        Board[x][y] = Symbol #fills the square
        #if(self.CheckWinCondition(Board, [x, y], Symbol, Win_Condition)):
         #   return True
        #return False

    """Checks if board is in a winning state for one of the players"""
    def CheckWinCondition(self, Board: list, Coordinates: tuple, Symbol: str):
        """Board: Array of arrays that represents the playing board
        Coordinates: Tuple that represents last move.
        Symbol: Represent players symbol (X/O)
        Win_Condition: int representing how many symbols in a straight line it takes to win
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1) ,(-1, 1), (1, -1)] #directions that will be checked for win condition (right, left, up, down, top-right, bottom-left, bottom-right, top-left)
        for i in range(0, 7, 2 ): #4 cycles for every column, row and diagonal.
            count = 0
            count += self.SearchInADirection(Board, directions[i], Symbol, [Coordinates[0], Coordinates[1]])
            count += self.SearchInADirection(Board, directions[i + 1], Symbol, [Coordinates[0], Coordinates[1]])
            count -= 1 #1 is substracted because the symbol on starting coordinates is counted twice
            if(count >= self.Win_Condition):
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