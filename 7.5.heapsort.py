class Heap:
    def __init__(self, n, S):
        # Complete the code here

def siftdown(H, i):
    # Complete the code here
        
def root(H):
    # Complete the code here

def removekeys(n, H, S):
    # Complete the code here

def makeheap(n, H):
    # Complete the code here

def heapsort(n, H, S):
    # Complete the code here


# Example 1
print("######Example 1######") 
n = 6
S = [0] + [10, 7, 11, 5, 13, 8]
heap = Heap(n, S)
heapsort(n, heap, S)
print("sorted S:", S)
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######") 
n = 10
S = [0] + [10,9,8,7,6,5,4,3,2,1]
heap = Heap(n, S)
heapsort(n, heap, S)
print("sorted S:", S)
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
# n =
# S = 
raise NotImplementedError("Complete your example.")
heap = Heap(n, S)
heapsort(n, heap, S)
print("sorted S:", S)
print(f"{'-'*20}\n")
