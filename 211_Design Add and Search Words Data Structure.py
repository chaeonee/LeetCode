from collections import deque

class Node:
    def __init__(self, value=None):
        self.value = value
        self.child = {}
        self.word = None

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        head = self.root
        for w in word:
            if w not in head.child.keys():
                head.child[w] = Node(w)
            head = head.child[w]
        head.word = word
        

    def search(self, word: str) -> bool:
        nodes = deque([self.root])
        for w in word:
            h_len = len(nodes)
            for _ in range(h_len):
                node = nodes.popleft()
                if w == '.':
                    for _, n in node.child.items():
                        nodes.append(n)
                else:
                    if w in node.child.keys():
                        nodes.append(node.child[w])
        
        for n in nodes:
            if n.word:
                return True
                
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
