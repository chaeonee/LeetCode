# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def check(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> int:
        if a and b:
            return 1
        elif not a and not b:
            return 0
        return -1

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        c_val = self.check(p, q)
        if c_val == 0:
            return True
        elif c_val == -1:
            return False
            
        t1, t2 = deque([p]), deque([q])
        while t1 and t2:
            n1, n2 = t1.popleft(), t2.popleft()
            if n1.val != n2.val:
                return False

            c_val = self.check(n1.left, n2.left)
            if c_val == -1:
                return False
            elif c_val == 1:
                t1.append(n1.left)
                t2.append(n2.left)

            c_val = self.check(n1.right, n2.right)
            if c_val == -1:
                return False
            elif c_val == 1:
                t1.append(n1.right)
                t2.append(n2.right)
            
        return True if not t1 and not t2 else False
        
