h,w = map(int,input().split())
a =[list(map(int,(input().split()))) for _ in range(h)]
vertical = [0 for i in range(h)]
horizontal = [0 for i in range(w)]
for i in range(h):
    vertical[i] = sum(a[i])
for i in range(w):
    cnt = 0
    for j in range(h):
        cnt += a[j][i]
    horizontal[i] = cnt
for i in range(h):
    for j in range(w):
        print(vertical[i]+horizontal[j]-a[i][j],end = " ")
    print()
