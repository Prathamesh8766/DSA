class Treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]


root = Treenode(1)
child1 = Treenode(2)
child2 = Treenode(3)
child3 = Treenode(4)



root.children.extend([child1,child2,child3])

child2.children.extend([Treenode(7),Treenode(8)])


def print_tree(root):
    if root is None:
        return
    
    print("Tree val is ",root.data)

    for child in root.children:
        print("Tree val is ",child.data)
        # print_tree(child)

    # for child in root.children:
    #     print_tree(child)

    
# print_tree(root)


def take_input():
    data  = int(input("Enter the data for the node : "))
    node = Treenode(data)
    num_children = int(input("Enter the num number of children : "))
    for eachchild in range(num_children):
        child = take_input()
        node.children.append(child)
    return node

root = take_input()
print_tree(root)

