N,M = map(int,input().split())
field = []
for i in range(N):
    b = list(map(int,input().split()))
    field.append(b)
flag = True
for i in range(N):

    for j in range(M):
        if j >= 1 and field[i][j] != field[i][j-1]+1:
            flag = False
        if i >= 1 and field[i][j] != field[i-1][j] + 7:
            flag = False
        if j >= 1 and field[i][j-1]%7 == 0 and field[i][j]%7 == 1:
            flag = False
        
if flag:
    print('Yes')
else:
    print('No')