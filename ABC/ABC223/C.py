N = int(input())
time_cnt = 0
length = 0
field = []
for i in range(N):
    a,b = map(int,input().split())
    time_cnt += a/b
    field.append([a,b])
    length += a
time_cnt /= 2
cnt = 0
ans = 0
for i in range(N):
    if cnt + field[i][0]/field[i][1] > time_cnt:
        tmp = time_cnt-cnt
        ans += field[i][1] * tmp
        break
    else:
        cnt += field[i][0]/field[i][1]
        ans += field[i][0]
print(ans)