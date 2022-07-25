# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root , B):
        # BFS 
        ans = []
        if root.val == B :
            return ans
        queue = deque([(root , 0)])
        depth = None
        while queue :
            node , level = queue.popleft()
            if (node.left and node.left.val == B) or (node.right and node.right.val == B):
                # if found traget 
                # now search for siblings (same level / different parent) 
                depth = level + 1
                continue
            if level == depth : 
                # stop at same level  
                ans.append(node.val)
                continue
            if node.left :
                queue.append((node.left , level + 1))
            if node.right :
                queue.append((node.right , level + 1 ))
        return ans
                