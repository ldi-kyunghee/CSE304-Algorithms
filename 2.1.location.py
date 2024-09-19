def location(low, high, S, x):
    if low > high:
        return -1
    else:
        # Complete the code here
        
# Example 1
print("######Example 1######")
S = [5, 7, 8, 10, 11, 13]
x = 15 
result = location(0, len(S)-1, S, x)
print("location:", result)
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
S = [5, 7, 8, 10, 11, 13]
x = 10 
result = location(0, len(S)-1, S, x)
print("location:", result)
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
# S = 
# x = 
raise NotImplementedError("Complete your example.")
result = location(0, len(S)-1, S, x)
print("location:", result)
print(f"{'-'*20}\n")