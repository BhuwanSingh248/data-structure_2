
# need to recall again

def minimumRemoval(posA, posB, A, B, canSkip, n):
    global dp 
    
    if posA >= n or posB >= n:
        return 0
    
    if dp[posA][posB][canSkip] != -1:
        return dp[posA][posB][canSkip]
    
    op1 = 0
    op2 = 0
    op3 = 0

    if A[posA] == B[posB]:
        op1 = 1 + minimumRemoval(posA+1, posB+1, A, B, 0 , n)
    
    if canSkip:
        op2 = minimumRemoval(posA+1, posB, A,B, canSkip, n)
    
    op3 = minimumRemoval(posA, posB+1, A, B, canSkip, n)
    dp[posA][posB][canSkip] = max(op1, op2, op3)
    return dp [posA][posB][canSkip]

def minOperations(A, B, N):
    print(N - minimumRemoval(0, 0, A, B, 1, N))

A = "abab"
B = "baba"

dp = [[[-1, -1] for i in range(len(A))] for j in range(len(B))]
N = len(A)
minOperations(A, B, N)