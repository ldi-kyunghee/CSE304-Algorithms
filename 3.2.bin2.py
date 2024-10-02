import time

def bin2(n, k):
    B = [[0] * (k + 1) for _ in range(n + 1)]
    # Complete the code here

    return B[n][k]

# Example 1
print("######Example 1######")
n = 15
k = 7
stime = time.time()
answer = bin2(n, k)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")

# Example 2
print("######Example 2######")
n = 30
k = 10
stime = time.time()
answer = bin2(n, k)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")

# Example 3 - Your Custom Case 
print("######Example 3######") 
# Insert your example here
# n = 
raise NotImplementedError("Complete your example.")
stime = time.time()
answer = bin2(n)
etime = time.time() - stime
print("answer:", answer)
print("execution time:", round(etime,5))
print(f"{'-'*20}\n")