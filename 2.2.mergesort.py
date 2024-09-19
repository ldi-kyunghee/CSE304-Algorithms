def merge(h, m, U, V, S):
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    # Complete the code here

def mergesort(n, S):
    h = n // 2
    m = n - h
    if n > 1:
        # Complete the code here

# Example 1 for 'merge()'
print("######Example 1 for 'merge()'######")
U = [17, 19, 39, 41, 73] # sorted
V = [16, 22, 66, 94, 98] # sorted
h = len(U)
m = len(V)
S = [-1] * (h + m)
merge(h, m, U, V, S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'merge()'
print("######Example 2 for 'merge()'######") 
# Insert your example here
# U = 
# V = 
h = len(U)
m = len(V)
S = [-1] * (h + m)
raise NotImplementedError("Complete your example.")
merge(h, m, U, V, S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 1 for 'mergesort()'
print("######Example 1 for 'mergesort()'######")
S = [22, 98, 17, 16, 19, 73, 94, 41, 39, 66]
mergesort(len(S), S)
print("S:", S)
print(f"{'-'*20}\n")

# Example 2 - Your Custom Case for 'mergesort()'
print("######Example 2 for 'mergesort()'######") 
# Insert your example here
# S = 
raise NotImplementedError("Complete your example.")
mergesort(len(S), S)
print("S:", S)
print(f"{'-'*20}\n")
