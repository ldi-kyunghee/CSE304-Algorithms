def promising(i, weight, total):
    global n, W, w, include
    # Complete the code here

def sumofsubsets(i, weight, total):
    global n, W, w, include
    if promising(i, weight, total):
        if weight == W:
            print("found:", include[1:])
        else:
            # Complete the code here

# Example 1
print("######Example 1######")
n, W = 4, 13
w = [0, 3, 4, 5, 6]
include = [0] * (n + 1)
sumofsubsets(0, 0, sum(w[1:]))

# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# n, W = 
# w =
include = [0] * (n + 1)
raise NotImplementedError("Complete your example.")
sumofsubsets(0, 0, sum(w[1:]))
