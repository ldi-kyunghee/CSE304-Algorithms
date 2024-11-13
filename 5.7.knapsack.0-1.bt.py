def promising(i, weight, profit):
    global n, W, w, p, maxprofit
    # Complete the code here

    return bound > maxprofit
            
def knapsack(i, weight, profit):
    global n, W, w, p, bestset, include, maxprofit
    if weight <= W and profit > maxprofit:
        # Complete the code here
    if promising(i, weight, profit):
        # Complete the code here

# Example 1
print("######Example 1######")
n, W = 4, 16
w = [0] + [2, 5, 10, 5]
p = [0] + [40, 30, 50, 10]
bestset, include = [0] * (n + 1), [0] * (n + 1)
maxprofit = 0
knapsack(0, 0, 0)
print("maxprofit =",maxprofit)
print("bestset =",bestset)


# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# n, W = 
# w = [0] + 
# p = [0] + 
bestset, include = [0] * (n + 1), [0] * (n + 1)
maxprofit = 0
raise NotImplementedError("Complete your example.")
knapsack(0, 0, 0)
print("maxprofit =",maxprofit)
print("bestset =",bestset)
