def binsearch(n, S, x):
    low, high = 0, n-1
    location = -1
    # Complete the code here
    
    return location

# Example 1
print("######Example 1######")
S = [5, 7, 8, 10, 11, 13]
x = 15 
location = binsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
S = [5, 7, 8, 10, 11, 13]
x = 10 
location = binsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
# S = 
# x = 
raise NotImplementedError("Complete your example.")
location = binsearch(len(S), S, x)
print("location:", location)
print(f"{'-'*20}\n")