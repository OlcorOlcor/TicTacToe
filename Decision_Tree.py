class Node:
    def __init__(self, parent, x: int, y: int):
        self.parent = parent
        self.x = x
        self.y = y
        self.children = []

    def Add_A_Child(self, child):
        self.children.append(child)


class Decision_Tree:
    def __init__(self, root):
        self.root = root