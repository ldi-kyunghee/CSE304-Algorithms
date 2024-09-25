class Matrix:
    
    def __init__(self, mat):
        self.n = len(mat)
        self.matrix = mat
    
    def __add__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                mat[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(mat)

    def __sub__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                mat[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(mat)

    def __mul__(self, other):
        mat = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    mat[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(mat)
            
def partition(n, M):
    m = n // 2
    m1 = [[0] * m for _ in range(m)]
    m2 = [[0] * m for _ in range(m)]
    m3 = [[0] * m for _ in range(m)]
    m4 = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            # Complete the code here

    return Matrix(m1), Matrix(m2), Matrix(m3), Matrix(m4)
    
def combine(n, M1, M2, M3, M4):
    m = n // 2
    mat = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            # Complete the code here

    return Matrix(mat)
   
def strassen(n, A, B):
    global threshold

    if n <= threshold:
        return A * B
    else:
        A11, A12, A21, A22 = partition(n, A)
        B11, B12, B21, B22 = partition(n, B)
        
        # Complete the code here

        return combine(n, C11, C12, C21, C22)

threshold = 1

# Example 1 for 'partition() and combine()'
print("######Example 1 for 'partition() and combine()'######")
n = 4
M = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]])
M11, M12, M21, M22 = partition(n, M)
combined_M = combine(n, M11, M12, M21, M22)

print(f"M11:")
for i in range(M11.n):
    print(M11.matrix[i])
print(f"M12:")
for i in range(M12.n):
    print(M12.matrix[i])
print(f"M21:")
for i in range(M21.n):
    print(M21.matrix[i])
print(f"M22:")
for i in range(M22.n):
    print(M22.matrix[i])
print(f"combined M:")
for i in range(combined_M.n):
    print(combined_M.matrix[i])
print(f"{'-'*20}\n")


# Example 2 - Your Custom Case for 'partition() and combine()'
print("######Example 2 for 'partition() and combine()'######")
# n = 
# M =
assert n >= 4
raise NotImplementedError("Complete your example.")
M11, M12, M21, M22 = partition(n, M)
combined_M = combine(n, M11, M12, M21, M22)

print(f"M11:")
for i in range(M11.n):
    print(M11.matrix[i])
print(f"M12:")
for i in range(M12.n):
    print(M12.matrix[i])
print(f"M21:")
for i in range(M21.n):
    print(M21.matrix[i])
print(f"M22:")
for i in range(M22.n):
    print(M22.matrix[i])
print(f"combined M:")
for i in range(combined_M.n):
    print(combined_M.matrix[i])
print(f"{'-'*20}\n")

# Example 1 for 'strassen()'
print("######Example 1 for 'strassen()'######")
n = 4
A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]])
B = Matrix([[8, 9, 1, 2], [3, 4, 5, 6], [7, 8, 9, 1], [2, 3, 4, 5]])

C = A * B
print("Standard Matrix Multiplication:")
for i in range(C.n):
    print(C.matrix[i])
C = strassen(n, A, B)
print("Strassen Matrix Multiplication:")
for i in range(C.n):
    print(C.matrix[i])
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'strassen()'
print("######Example 2 for 'strassen()'######") 
# Insert your example here
# n = 
# A = 
# B = 
assert n >= 4

C = A * B
print("Standard Matrix Multiplication:")
for i in range(C.n):
    print(C.matrix[i])
raise NotImplementedError("Complete your example.")
C = strassen(n, A, B)
print("Strassen Matrix Multiplication:")
for i in range(C.n):
    print(C.matrix[i])
print(f"{'-'*20}\n")