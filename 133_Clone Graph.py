'''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        q = deque([node])
        graph = Node(node.val)
        g_list = {1:graph}
        while q:
            n = q.popleft()
            if not n.neighbors:
                continue

            for neigh in n.neighbors:
                if neigh.val not in g_list.keys():
                    q.append(neigh)
                    g_list[neigh.val] = Node(neigh.val)
                g_list[n.val].neighbors.append(g_list[neigh.val])

        return g_list[node.val]
