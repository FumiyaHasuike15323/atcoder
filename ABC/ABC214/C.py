N = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
sum_li = []
ans_li = [0]*N
for k in range(2):
    for i in range(0,N):
        ans_li[i] = min(t[i],ans_li[i-1]+s[i-1])
for i in ans_li:
    print(i)