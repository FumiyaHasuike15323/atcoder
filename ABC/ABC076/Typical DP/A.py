N = int(input())
p = list(map(int,input().split()))
dp = [[0]*11000 for i in range(110)]
p_sum = sum(p)
dp[0][0] = 1
for i in range(len(p)):
    for j in range(p_sum):
        dp[i][p[i]] = 1
        if dp[i-1][j] == 1:
            dp[i][j] = 1
            dp[i][j+p[i]] = 1
print(dp[i].count(1))
