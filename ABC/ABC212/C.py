import bisect
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
ans = 10000000000000
cnt2 = 10000000000000
for i in range(n):
    left_idx = bisect.bisect_left(b,a[i])
    if left_idx == 0:
        left_idx += 1
    cnt1 = abs(a[i]-b[left_idx-1])
    if left_idx != len(b):
        cnt2 = abs(a[i]-b[left_idx])
    ans = min(cnt1,cnt2,ans)
print(ans)