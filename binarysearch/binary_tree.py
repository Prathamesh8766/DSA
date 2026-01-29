# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# from typing import Optional


# class TreeNode:
#     def __init__(self,val=0,left= None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right

# def binarytree():
#     val = input("Enter node value (-1 for no node): ")
#     if val == "-1":
#         return None

#     node = TreeNode(int(val))
#     print(f"Enter left child of {node.val}")
#     node.left = binarytree()

#     print(f"Enter right child of {node.val}")
#     node.right = binarytree()

#     return node

# def preorder(node):
#     if not node:
#         return
#     print(node.val, end=" ")
#     preorder(node.left)
#     preorder(node.right)


# root=binarytree()
# preorder(root)



# def isValidBST(root):
#     stack = []
#     prev_val = float('-inf')

#     while stack or root:
       
#         while root:
#             stack.append(root)
#             root = root.left

#         root = stack.pop()
        
#         if root.val <= prev_val:
#             return False
#         prev_val = root.val

#         root = root.right

#     return True

# print(isValidBST(root))
       