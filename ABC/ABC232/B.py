s = input()
t = input()
cnt = 0
ans = 0
for i in range(1,27):
    cnt = 0
    for j in range(len(s)):
        chr_number = ord(s[j])
        if chr_number+i > 122:
            chr_number = chr_number-26
        if chr(chr_number+i) == str(t[j]):
            cnt += 1
            ans = max(cnt,ans)
if ans == len(s):
    print('Yes')
else:
    print('No')