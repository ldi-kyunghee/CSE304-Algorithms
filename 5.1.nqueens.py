def promising(i, n, col):
    is_promising = True
    # Complete the code here

    return is_promising

def nqueens(i, n, col):
    if promising(i, n, col):
        if i == n:
            print("found=", col[1:])
        else:
            # Complete the code here

# Example 1
print("######Example 1######")
n = 4
col = [0] * (n + 1)
nqueens(0, n, col)

# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# n = 
col = [0] * (n + 1)
raise NotImplementedError("Complete your example.")
nqueens(0, n, col)