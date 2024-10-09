class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def preorder(self, path):
        path.append(self.key)
        if self.left != None:
            self.left.preorder(path)
        if self.right != None:
            self.right.preorder(path)

    def inorder(self, path):
        if self.left != None:
            self.left.inorder(path)
        path.append(self.key)
        if self.right != None:
            self.right.inorder(path)
                
def minimum(i, j, A, p):
    minvalue, mink = INF, 0
    for k in range(i, j + 1):
        # Complete the code here
    
    return minvalue, mink

def optsearchtree(n, p):
    A = [[INF] * (n + 1) for _ in range(n + 2)]
    R = [[0] * (n + 1) for _ in range(n + 2)]
    for i in range(1, n + 1):
        A[i][i - 1] = R[i][i - 1] = 0
        A[i][i], R[i][i] = p[i], i
    A[n + 1][n] = R[n + 1][n] = 0

    for diagonal in range(1, n):
        # Complete the code here
        # Tip. Implement minimum() and use it

    return A[1][n], A, R

def tree(i, j, K, R):
    k = R[i][j]
    if k == 0:
        return None
    else:
        # Complete the code here
        return p

INF = float("inf")

# Example 1
print("######Example 1######")
n = 4
K = [0, 10, 20, 30, 40]
p = [0, 3, 3, 1, 1]
minavg, A, R = optsearchtree(n, p)
print("A = ")
for i in range(1, n + 2):
    print(A[i][i-1:])
print("R = ")
for i in range(1, n + 2):
    print(R[i][i-1:])
print("minavg = ", minavg)

root = tree(1, n, K, R)
path = [] 
root.preorder(path)
print("preorder=", path)
path = []
root.inorder(path)
print("inorder=", path)


# # Example 2 - Your Custom Case
# print("######Example 2 #######") 
# # Insert your example here
# n = 
# K = 
# p = 
raise NotImplementedError("Complete your example.")
minavg, A, R = optsearchtree(n, p)
print("A = ")
for i in range(1, n + 2):
    print(A[i][i-1:])
print("R = ")
for i in range(1, n + 2):
    print(R[i][i-1:])
print("minavg = ", minavg)

root = tree(1, n, K, R)
path = [] 
root.preorder(path)
print("preorder=", path)
path = []
root.inorder(path)
print("inorder=", path)