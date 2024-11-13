def promising(i):
    global W, vcolor
    # Complete the code here

    return True
    
def mcoloring(i, m):
    global n, vcolor, count
    if promising(i):
        if i == n:
            print(vcolor[1:])
            # Complete the code here
        else:
            # Complete the code here

# Example 1
print("######Example 1######")
m = 3
n = 4
count = 0
vcolor = [0] * (n + 1)
W = [[0,0,0,0,0],
     [0,0,1,1,1], # (1,2), (1,3), (1,4)
     [0,1,0,1,0], # (2,1), (2,3)
     [0,1,1,0,1], # (3,1), (3,2), (3,4)
     [0,1,0,1,0]] # (4,1), (4,3)
mcoloring(0, m)
print("count =",count)


# Example 2 - Your Custom Case
print("######Example 2 #######") 
# Insert your example here
# m = 
# n = 
# W = 
count = 0
vcolor = [0] * (n + 1)
raise NotImplementedError("Complete your example.")
mcoloring(0, m)
print("count =",count)