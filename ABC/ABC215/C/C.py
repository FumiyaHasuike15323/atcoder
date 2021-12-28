import itertools
s,k = map(str,input().split())
k = int(k)
s = list(s)
ans_li = list(itertools.permutations(s,len(s)))
ans_li = sorted(set(ans_li))
print("".join(list(ans_li[k-1])))