import itertools
import collections
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
B_C = []
for i in range(N):
    B_C.append(B[C[i]-1])
dic_A = collections.Counter(A)
dic_B_C = collections.Counter(B_C)
ans = 0
for key in list(dic_A):
    if dic_B_C[key] != None:
        ans += dic_B_C[key]*dic_A[key]
print(ans)