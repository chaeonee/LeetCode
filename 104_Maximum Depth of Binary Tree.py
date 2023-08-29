# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0
        
        q = deque()
        if root:
            q.append(root)
            
        while q:
            d += 1
            l = len(q)
            for _ in range(l):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return d
