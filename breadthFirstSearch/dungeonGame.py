game = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
    ]

dp = [[None] * len(game) for i in range(len(game[0]))]
R, C = len(game), len(game[0]) 

for i in range(R-1, -1,-1):
    for j in range(C-1, -1,-1):
        if i == R-1 and j == C-1 :
            dp[i][j] = min(0, game[i][j])
        elif i == R-1 :
            dp[i][j] = min(0, game[i][j] + dp[i][j+1] )
        elif j == C-1:
            dp[i][j] = min(0, game[i][j] + dp[i+1][j])

        else:
            dp[i][j] = min(0, game[i][j]+max(dp[i][j+1], dp[i+1][j]))
print(dp)

