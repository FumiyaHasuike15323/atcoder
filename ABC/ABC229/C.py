n,w = map(int,input().split())
cheese =[]
for i in range(n):
    a,b = map(int,input().split())
    cheese.append([a,b])
cheese.sort(reverse=True)
ans = 0
cnt = 0
for i in range(n):
    if cnt + cheese[i][1] <= w:
        cnt += cheese[i][1]
        ans += cheese[i][0]* cheese[i][1]
    else:
        rest = w-cnt
        ans += cheese[i][0] * rest
        break
print(ans)

    