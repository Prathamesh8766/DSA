from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = Queue()
        result = []

        def levelorder(root):
            if not root:
                return []
            
            queue.enqueue(root)

            while not queue.is_empty():
                size = len(queue)
                current_level_value = []
                for _ in range(size):
                    current = queue.dequeue()
                    current_level_value.append(current.val)
                    if current.left is not None:
                        queue.enqueue(current.left)
                    if current.right is not None:
                        queue.enqueue(current.right)

                result.append(current_level_value)
            return result

        return levelorder(root)
 

# using Recursive 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        def bfs(root ,level):
            if not root:
                return []

            if len(result) == level:
                result.append([])


            result[level].append(root.val)

            bfs(root.left,level+1)
            bfs(root.right,level+1)

        bfs(root,0)
        return result 

