import itertools
n,m = map(int,input().split())
field = [[]*n for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    field[a].append(b)
    field[b].append(a)
visited = [False]*n
li = [x for x in range(n)]

permutations_lis = itertools.permutations(li)
ans = 0

for line in permutations_lis:
    if line[0] != 0:continue
    for i in range(n-1):
        if field[line[i]].count(line[i+1]) == 0:
            break
    if field[line[i]].count(line[i+1]) == 0:continue
    ans += 1
print(ans)