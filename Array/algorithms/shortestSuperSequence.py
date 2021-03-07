def findSubsequence(str1, str2):
    n = len(str1)+1
    m = len(str2)+1
    substr = ""
    memo = [[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            
            if i == 0 or j == 0:
               memo[i][j] = 0 
            
            elif str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    while i >= 0 and j >= 0 :
        a = memo[i][j]
        b = memo[i-1][j]
        c = memo[i][j-1]
        d = memo[i-1][j-1]

        if b == c == d != a:
            substr += str1[i-1]
            i = i-1
            j = j-1
        elif b > c:
            i = i-1
        elif b < c:
            j = j-1
        else:
            i = j - 1    
    return memo[n-1][m-1], substr[::-1]

def superSequence(str1, str2):
    subSeq = findSubsequence(str1, str2)[1]
    i = 0 
    j = 0
    supseq = ""
    for s in subSeq:
        while str1[i] != s:
            supseq += str1[i]
            i+=1
        while str2[j] != s:
            sups
            eq += str2[j]
            j+=1
        supseq += s
        i+=1
        j+=1
    supseq += str1[i:]+str2[j:]
    return supseq
a = "BHGDFHSKYSK"
b = "BHGTYSK"   
# BHGDFHSKYSK                   

print(superSequence(a,b))