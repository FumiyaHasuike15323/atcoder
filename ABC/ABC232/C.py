n,m = map(int,input().split())
takahashi = [[] for i in range(n)]
aoki = [[] for i in range(n)]
len_taka =[]
len_aoki = []
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    takahashi[a].append(b)
    takahashi[b].append(a)
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    aoki[a].append(b)
    aoki[b].append(a)
for i in range(len(takahashi)):
    len_taka.append(len(takahashi[i]))
    len_aoki.append(len(aoki[i]))
len_taka.sort()
len_aoki.sort()
for i in range(len(len_taka)):
    if len_taka[i] != len_aoki[i]:
        print('No')
        exit()
print('Yes')