from heapq import heappush, heappop

class Node:

    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        
    def preorder(self, path):
        path.append((self.symbol, self.freq))
        if self.left != None:
            self.left.preorder(path)
        if self.right != None:
            self.right.preorder(path)

    def inorder(self, path):
        if self.left != None:
            self.left.inorder(path)
        path.append((self.symbol, self.freq))
        if self.right != None:
            self.right.inorder(path)

def huffman(n, s, f):
    heap = []
    for i in range(n):
        heappush(heap, (f[i], Node(s[i], f[i])))

    # Complete the code here

    return heappop(heap)[1]

# Example 1
print("######Example 1######")
n = 6
s = ['b', 'e', 'c', 'a', 'd', 'f']
f = [5, 10, 12, 16, 17, 25]
root = huffman(n, s, f)
path = []
root.preorder(path)
print("preorder= ",path)
path = []
root.inorder(path)
print("inorder= ",path)



# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# n = 
# s = 
# f = 
raise NotImplementedError("Complete your example.")
root = huffman(n, s, f)
path = []
root.preorder(path)
print("preorder= ",path)
path = []
root.inorder(path)
print("inorder= ",path)
