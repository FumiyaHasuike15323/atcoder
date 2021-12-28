import math
n = int(input())
cnt = 0
for a in range(1,n+2):
    if a*a*a > n:
        print(cnt)
        exit()
    for b in range(a,n+2):
        if a*b*b > n:
            break
        cnt += n//(a*b)-b+1
