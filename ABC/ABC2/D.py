import itertools
n,m = map(int,input().split())
friends = [[0]*(n+1) for j in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    friends[x][y] = 1
    friends[y][x] = 1
ans = -1
for bit in range(2**n):
    group = []
    for j in range(n):
        if (bit >> j) & 1:
            group.append(j+1)
    flag = 0
    for li in itertools.combinations(group,2):
        if friends[li[0]][li[1]] == 0:
            flag = 1
            break
    if flag == 0:
        cnt = len(group)
        ans = max(ans,cnt)
print(ans)
