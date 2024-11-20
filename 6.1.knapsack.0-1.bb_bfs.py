class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit

def boundof(u, n, W, w, p):
    if u.weight >= W:
        return 0
    else:
        # Complete the code here

def knapsack2(n, W, w, p):
    global count
    queue = [] # Initialize Queue
    v = Node(0, 0, 0)
    bound = boundof(v, n, W, w, p)
    maxprofit = 0
    queue.append(v)
    count+=1
    while len(queue) != 0:
        # Complete the code here

    return maxprofit

# Example 1
print("######Example 1######")
n, W = 4, 16
w = [0] + [2, 5, 10, 5]
p = [0] + [40, 30, 50, 10]
count = 0
maxprofit = knapsack2(n, W, w, p)
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
maxprofit = knapsack2(n, W, w, p)
print("maxprofit =",maxprofit)
print("count =",count)