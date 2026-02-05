class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None   

    def preOrder(self, root):
        if root is None:
            return

        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)
    def postOrder(self,root) :
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data ,end=" ")

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

root.left.left = Tree(4)
root.left.right = Tree(5)

root.right.left = Tree(6)
root.right.right = Tree(7)


root.preOrder(root)
print()
root.inOrder(root)
print()
root.postOrder(root)
