import itertools
n = int(input())
k = int(input())
li = [int(input()) for _ in range(n)]
li_ans = set()
ans = 0
permutations_li = itertools.permutations(li,k)
for one_case in permutations_li:
    number = ""
    for i in range(k):
        number += str(one_case[i])
    li_ans.add(int(number))
print(len(li_ans))