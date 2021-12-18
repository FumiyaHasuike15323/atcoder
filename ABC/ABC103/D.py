n,m = map(int,input().split())
ls = []
for i in range(m):
    a,b = map(int,input().split())
    ls.append([a,b])
l = 0
ans = 0
ls = sorted(ls, key=lambda x :x[1])
for a,b in ls:
    if a >= l:
        l = b
        ans += 1
print(ans)