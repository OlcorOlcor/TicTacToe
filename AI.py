from Board import Board

class AI:

    def __init__(self, Win_Condition):
        self.Win_Condition = Win_Condition
        self.Board = Board()
        self.MaxDepth = 3

    """Starts the minimax algorithm, makes the best move for the given position"""
    def CalculateMove(self, Board, Symbol):
        """
        Board: Array of arrays representing the playing board
        Symbol: Represent the player (or AI)
        """
        depth = 0
        if(Symbol == 'X'):
            bestScore = -1000
        else:
            bestScore = 1000
        for r in range(1, len(Board)):
            for c in range(1, len(Board)): # tries every position 
                if(Board[r][c] == '.'):
                    Board[r][c] = Symbol 
                    result = self.Board.CheckIfMoveWon(Board, r, c, self.Win_Condition)
                    if(result == 1):
                        return
                    if Symbol == 'X':
                        score = self.minimax(Board, False, 'O', depth + 1) #starts the minimax with a new position
                    else:
                        score = self.minimax(Board, True, 'X', depth + 1) #starts the minimax with a new position
                    Board[r][c] = '.' #goes back to the original board
                    if Symbol == 'X':
                        if(score > bestScore): #if the score is better for the player, saves the move
                            bestScore = score
                            bestMove = (r, c)
                    else:
                        if(score < bestScore): #if the score is better for the player, saves the move
                            bestScore = score
                            bestMove = (r, c)
        Board[bestMove[0]][bestMove[1]] = Symbol #Plays the best move
    
    """The minimax algorithm, recusively calculates scores"""
    def minimax(self, Board, isMax, Symbol, depth):
        """
        Board: Array of arrays representing the playing board
        isMax: Bool representing if the maximizing or the minimizing player is on the move
        Symbol: Represent the player (or AI)
        """
        if(depth > self.MaxDepth ): #if depth is greater than the MaxDepth return Tie state
            return 0
        isFull = True
        if (isMax): #finds the best score for maximizing player
            bestScore = -100
            bestPossibleScore = 1
            for r in range(1, len(Board)):
                for c in range(1, len(Board)):
                    if(Board[r][c] == '.'):
                        isFull = False
                        Board[r][c] = Symbol
                        result = self.Board.CheckIfMoveWon(Board, r, c, self.Win_Condition)
                        if(result == 1):
                            Board[r][c] = '.'
                            return 1
                        score = self.minimax(Board, False, 'O', depth + 1)
                        Board[r][c] = '.'
                        bestScore = max(score, bestScore)
                        if(bestPossibleScore == bestScore): #if best scores is equal to bestPossibleScore, return bestScore, because the other positions can't get better than this.
                            return bestScore

        else: #finds the best score for minimizing player
            bestScore = 100
            bestPossibleScore = -1
            for r in range(1, len(Board)):
                for c in range(1, len(Board)):
                    if(Board[r][c] == '.'):
                        isFull = False
                        Board[r][c] = Symbol
                        result = self.Board.CheckIfMoveWon(Board, r, c, self.Win_Condition)
                        if(result == 1):
                            Board[r][c] = '.'
                            return -1
                        score = self.minimax(Board, True, 'X', depth + 1)
                        Board[r][c] = '.'
                        bestScore = min(score, bestScore)
                        if(bestPossibleScore == bestScore):#if best scores is equal to bestPossibleScore, return bestScore, because the other positions can't get better than this.
                            return bestScore
        if(isFull == True): #the board is full - tie
            return 0
        return bestScore


