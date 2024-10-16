def dijkstra(n, W):
    F = []
    for i in range(2, n + 1):
        touch[i] = 1
        length[i] = W[1][i]
    for _ in range(n - 1):
        # Complete the code here

    return F
                
INF = float("inf")

# Example 1
print("######Example 1######")
n = 5 # the number of vertices
W = [ # adjacency matrix
        [INF,    INF,      INF,    INF,      INF,      INF],
        [INF,      0,        7,      4,        6,        1],
        [INF,    INF,        0,     INF,     INF,      INF],
        [INF,    INF,        2,      0,        5,      INF],
        [INF,    INF,        3,    INF,        0,      INF],
        [INF,    INF,      INF,    INF,        1,        0]
    ]
touch = [-1] * (n + 1)
length = [-1] * (n + 1)

F = dijkstra(n, W)
print(F)



# # Example 2 - Your Custom Case
# print("######Example 2 #######") 
# # Insert your example here
# n =   
# W = 
touch = [-1] * (n + 1)
length = [-1] * (n + 1)
raise NotImplementedError("Complete your example.")

F = dijkstra(n, W)
print(F)