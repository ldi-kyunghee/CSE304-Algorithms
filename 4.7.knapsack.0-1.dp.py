def knapsack(n, W, DP):
    global w, p
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        # Complete the code here

    return DP[(n, W)]
    

# Example 1
print("######Example 1######")
n, W = 3, 30
w = [0, 5, 10, 20]
p = [0, 50, 60, 140]
DP = {}
maxprofit = knapsack(n, W, DP)
print("maxprofit: ", maxprofit)

# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# n, W =
# w =
# p =
raise NotImplementedError("Complete your example.")
DP = {}
maxprofit = knapsack(n, W, DP)
print("maxprofit: ", maxprofit)