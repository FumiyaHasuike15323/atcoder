import collections
N = int(input())
a = list(map(int,input().split()))
li = collections.Counter(a)
li_key = list(li.keys())
ans = 0
for i in range(len(li_key)):
    for j in range(i+1,len(li_key)):
        ans += (li[li_key[i]] * li[li_key[j]])*((li_key[i]-li_key[j])**2)
print(ans)