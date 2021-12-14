import sys
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())
edge = [[]for _ in range(n)]
seen = [False]*n
for i in range(m):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

def dfs(node,prev):
    seen[node] = True
    for next_ in edge[node]:
        if next_ == prev:continue
        if seen[next_]:return False
        if not dfs(next_,node):return False
    return True

ans = 0
while False in seen:
    start = seen.index(False)
    if dfs(start,-1):ans += 1
print(ans)