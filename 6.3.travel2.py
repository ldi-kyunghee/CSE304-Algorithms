from heapq import heappush, heappop
import time

class Node:
    def __init__(self, level, path):
        self.level = level
        self.path = path[:]
        self.bound = 0

def remainder(path, n):
    return n * (n + 1) // 2 - sum(path)

def pathlength(path, W):
    # Complete the code here

    return length

def hasOutgoing(v, path):
    return v in path[:len(path)-1]

def hasIncoming(v, path):
    return v in path[1:]

def boundof(v, n, W):
    global INF
    lower = pathlength(v.path, W)
    for i in range(1, n + 1):
        # Complete the code here

    return lower

def travel2(n, W):
    global INF
    heap = [] # Initialize Priority Queue
    v = Node(0, [1])
    v.bound = boundof(v, n, W)
    minlength, opttour = INF, []
    heappush(heap, (v.bound, time.time(), v))
    while len(heap) != 0:
        v = heappop(heap)[2]
        if v.bound < minlength:
            for i in range(2, n + 1):
                # Complete the code here
                
    return minlength, opttour
    
INF = float("inf")



# Example 1
print("######Example 1######")
n = 5
W = [[INF, INF, INF, INF, INF, INF],
    [INF, 0, 14, 4, 10, 20],
    [INF, 14, 0, 7, 8, 7],
    [INF, 4, 5, 0, 7, 16],
    [INF, 11, 7, 9, 0, 2],
    [INF, 18, 7, 17, 4, 0]]
    
minlength, opttour = travel2(n, W)
print("minlength:", minlength)
print("opttour:", opttour)


# Example 2
print("######Example 2######")
# Insert your example here
# n = 
# W = 
raise NotImplementedError("Complete your example.")
minlength, opttour = travel2(n, W)
print("minlength:", minlength)
print("opttour:", opttour)