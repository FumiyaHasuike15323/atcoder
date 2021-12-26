N = list(input())
len_N = len(N)
ans = 0
for i in range(2 ** len_N):
    a = []
    b = []
    for j in range(len_N):
        if ((i >> j) & 1):
            a.append(N[j])
        else:
            b.append(N[j])
    a.sort(reverse=True)
    b.sort(reverse=True)
    if len(a) == 0 or len(b) == 0:continue
    if a[0] != 0 or b[0] != 0:
        value_a = int("".join(a))
        value_b = int("".join(b))
        ans = max(ans,int(value_a)*int(value_b))
print(ans)