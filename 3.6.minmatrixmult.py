def minimum(i, j, M, d):
    minvalue, mink = INF, 0
    for k in range(i, j):
        # Complete the code here

    return minvalue, mink

def minmult(n, d):
    M = [[INF] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][i] = 0
    for diagonal in range(1, n):
        # Complete the code here
        # Tip. Implement minimum() and use it

    return M[1][n], M, P

def order(i, j, P):
    if i == j:
        return "A" + str(i)
    else:
        # Complete the code here  

INF = float("inf")

# Example 1
print("######Example 1######")
n = 6
d = [5, 2, 3, 4, 6, 7, 8]
minvalue, M, P = minmult(n, d)
print("M = ")
for i in range(1, n + 1):
    print(M[i][i:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][i:])
print("minmult = ", minvalue)

multorder = order(1, n, P)
print(multorder)


# # Example 2 - Your Custom Case
# print("######Example 2 #######") 
# # Insert your example here
# n = 
# d = 
raise NotImplementedError("Complete your example.")
minvalue, M, P = minmult(n, d)
print("M = ")
for i in range(1, n + 1):
    print(M[i][i:])
print("P = ")
for i in range(1, n + 1):
    print(P[i][i:])
print("minmult = ", minvalue)

multorder = order(1, n, P)
print(multorder)