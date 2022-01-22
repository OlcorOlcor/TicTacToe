from Game import Game
from AI import AI
from Decision_Tree import Decision_Tree
from Decision_Tree import Node
game = Game()
#game.MenuLoop()

b = game.CreatePlayingBoard(5)

a = AI(Decision_Tree(Node(None, None, None)))
a.Build_Decision_Tree(b, 'X', 3, a.tree.root)

print()