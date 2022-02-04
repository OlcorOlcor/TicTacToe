import os

class Board():
    
    
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
    
    """Displays board in console"""
    def ResetBoard(self, Board):
        clear = lambda: os.system('cls')
        clear()
        for r in Board:
            print("".join(r))

    """Checks if a game is a in winning or drawing state"""
    def CheckWinningState(self, Board, Win_Condition) -> int:
        """
        Board: Array of arrays that represents the playing board
        Win_Condition: integer representing the win condition
        """
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
                if(col_sum >= Win_Condition or row_sum >= Win_Condition):
                    return 1
                elif(-col_sum >= Win_Condition or -row_sum >= Win_Condition):
                    return -1
            #checks diagonal
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
            if(diag1_sum >= Win_Condition or diag2_sum >= Win_Condition):
                    return 1
            elif(-diag1_sum >= Win_Condition or -diag2_sum >= Win_Condition):
                return -1
        if(isFull):
            return 0
        else:
            return None