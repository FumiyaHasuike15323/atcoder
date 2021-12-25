import itertools
n,m = map(int,input().split())
takahashi = [[-1]*n for i in range(n)]
aoki = [[-1]*n for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    takahashi[a][b] = 1
    takahashi[b][a] = 1
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    aoki[a][b] = 1
    aoki[b][a] = 1

for ele in list(itertools.permutations(range(n))):
    ans = True
    for j in range(n):
        for k in range(n):
            if takahashi[j][k] != aoki[ele[j]][ele[k]]:
                ans = False
    if ans == True:
        print('Yes')
        exit()
print('No')