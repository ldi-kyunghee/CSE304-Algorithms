def prim(n, W):
    F = []
    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]
    for _ in range(n - 1):
        # Complete the code here

    return F
                
INF = float("inf")

# Example 1
print("######Example 1######")
n = 5 # the number of vertices
W = [ # adjacency matrix
        [INF,    INF,    INF,    INF,    INF,     INF],
        [INF,      0,      1,      3,    INF,     INF], 
        [INF,      1,      0,      3,      6,     INF],
        [INF,      3,      3,      0,      4,       2],
        [INF,    INF,      6,      4,      0,       5],
        [INF,    INF,    INF,      2,      5,       0]
    ]
nearest = [-1] * (n + 1)
distance = [-1] * (n + 1)

F = prim(n, W)
print(F)

# # Example 2 - Your Custom Case
# print("######Example 2 #######") 
# # Insert your example here
# n =   
# W = 
nearest = [-1] * (n + 1)
distance = [-1] * (n + 1)
raise NotImplementedError("Complete your example.")
F = prim(n, W)
print(F)