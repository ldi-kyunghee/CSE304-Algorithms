from heapq import heappush, heappop

class Item:
    def __init__(self, id, weight, profit):
        self.id = id
        self.weight = weight
        self.profit = profit
        self.profit_per_weight = profit // weight
        
def knapsack(n, W, w, p):
    heap = []
    for i in range(n):
        item = Item(i + 1, w[i], p[i])
        heappush(heap, (-item.profit_per_weight, item))
    maxprofit = total_weight = 0

    # Complete the code here

    return maxprofit

# Example 1
print("######Example 1######")
n, W = 3, 30
w = [5, 10, 20]
p = [50, 60, 140]
maxprofit = knapsack(n, W, w, p)
print("maxprofit: ", maxprofit)

# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# n, W =
# w =
# p =
raise NotImplementedError("Complete your example.")
maxprofit = knapsack(n, W, w, p)
print("maxprofit: ", maxprofit)