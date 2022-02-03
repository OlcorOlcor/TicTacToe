from numpy import equal
from Decision_Tree import Decision_Tree
from Decision_Tree import Node


class AI:


    def __init__(self, Win_Condition):
        self.Win_Condition = Win_Condition


    def CalculateMove(self, Board, Symbol):
        self.NumberOfMoves = 1
        bestScore = -1000
        for r in range(1, len(Board)):
            for c in range(1, len(Board)):
                if(Board[r][c] == '.'):
                    Board[r][c] = Symbol
                    score = self.minimax(Board, False, 'O')
                    Board[r][c] = '.'
                    if(score > bestScore):
                        bestScore = score
                        bestMove = (r, c)
        Board[bestMove[0]][bestMove[1]] = Symbol
    
    
    def minimax(self, Board, isMax, Symbol):
        result = self.CheckWinningState(Board)
        if(result is not None):
            return result
        if (isMax):
            bestScore = -100
            for r in range(1, len(Board)):
                for c in range(1, len(Board)):
                    if(Board[r][c] == '.'):
                        Board[r][c] = Symbol
                        score = self.minimax(Board, False, 'O')
                        Board[r][c] = '.'
                        bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = 100
            for r in range(1, len(Board)):
                for c in range(1, len(Board)):
                    if(Board[r][c] == '.'):
                        Board[r][c] = Symbol
                        score = self.minimax(Board, True, 'X')
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
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)] #directions that will be checked for win condition (right, left, up, down, top-right, bottom-left, bottom-right, top-left)
        for i in range(0, 7, 2 ): #4 cycles for every column, row and diagonal.
            count = 0
            count += self.SearchInADirection(Board, directions[i], Symbol, Coordinates[:])
            count += self.SearchInADirection(Board, directions[i + 1], Symbol, Coordinates[:])
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
    
    def CheckWinningStateDynamic(self, Board):
        diag1_sum = 0
        diag2_sum = 0
        length = len(Board)
        isFull = True
        for r in range(1, len(Board)):
            row_sum = 0
            col_sum = 0
            for c in range(1, len(Board)):
                #checks rows
                if(Board[r][c] == 'X'): 
                    row_sum += 1
                if(Board[r][c] == 'O'):
                    row_sum -= 1
                if(Board[r][c] == '.'):
                    isFull = False
                    row_sum = 0 

                #checks columns
                if(Board[c][r] == 'X'):
                    col_sum += 1
                if(Board[c][r] == 'O'):
                    col_sum -= 1
                if(Board[c][r] == '.'):
                    col_sum = 0
                
                #checks winning state
                if(col_sum >= self.Win_Condition or row_sum >= self.Win_Condition):
                    return 1
                elif(-col_sum >= self.Win_Condition or -row_sum >= self.Win_Condition):
                    return -1
            if(Board[r][r] == 'X'): 
                diag1_sum += 1
            if(Board[r][r] == 'O'):
                diag1_sum -= 1
            if(Board[r][r]== '.'):
                diag1_sum = 0
            if(Board[r][length - r] == 'X'): 
                diag2_sum += 1
            if(Board[r][length - r] == 'O'):
                diag2_sum -= 1
            if(Board[r][length - r]== '.'):
                diag2_sum = 0
            if(diag1_sum >= self.Win_Condition or diag2_sum >= self.Win_Condition):
                    return 1
            elif(-diag1_sum >= self.Win_Condition or -diag2_sum >= self.Win_Condition):
                return -1
        if(isFull):
            return 0
        else:
            return None