import itertools
field = []
n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    field.append([x,y])
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            ab_x = field[i][0] - field[j][0]
            ab_y = field[i][1] - field[j][1]
            ac_x = field[i][0] - field[k][0]
            ac_y = field[i][1] - field[k][1]
            if ab_x*ac_y - ab_y*ac_x == 0:
                continue
            cnt += 1
print(cnt)