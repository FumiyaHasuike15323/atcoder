n = int(input())
ls = []
for i in range(n):
    x,l = map(int,input().split())
    ls.append([x-l,x+l])
ls = sorted(ls,key=lambda x:x[1])
ans = n
for i in range(1,n):
    if ls[i-1][1] > ls[i][0]:
        ls[i][1] = ls[i-1][1]
        ans -= 1
print(ans)