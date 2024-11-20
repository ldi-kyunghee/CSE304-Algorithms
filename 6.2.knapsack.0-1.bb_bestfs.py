from heapq import heappush, heappop
class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0

def boundof(u, n, W, w, p):
    if u.weight >= W:
        return 0
    else:
        # Complete the code here

def knapsack3(n, W, w, p):
    global count
    heap = [] # Initialize Priority Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    heappush(heap, (-v.bound, v))
    count +=1
    while len(heap) != 0:
        # Complete the code here

    return maxprofit

# Example 1
print("######Example 1######")
n, W = 4, 16
w = [0] + [2, 5, 10, 5]
p = [0] + [40, 30, 50, 10]
count = 0
maxprofit = knapsack3(n, W, w, p)
print("maxprofit =",maxprofit)
print("count =",count)



# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# n, W = 
# w = [0] + 
# p = [0] + 
raise NotImplementedError("Complete your example.")
count = 0
maxprofit = knapsack3(n, W, w, p)
print("maxprofit =",maxprofit)
print("count =",count)