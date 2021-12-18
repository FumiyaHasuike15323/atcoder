import bisect
n = int(input())
present = [list(map(int,input().split())) for i in range(n)]
present.sort(key= lambda x:(x[0],-x[1]))
dp = [float("inf") for i in range(n+10)]
for i in range(n):
    target = bisect.bisect_left(dp,present[i][1])
    dp[target] = present[i][1]
for i in range(n+10):
    if dp[i] == float("inf"):
        print(i)
        break