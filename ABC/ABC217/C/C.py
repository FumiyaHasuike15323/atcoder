N = int(input())
p = list(map(int,input().split()))
ans_li = [-1]*N
for i in range(len(p)):
    ans_li[p[i]-1] = i+1
for element in ans_li:
    if element == ans_li[-1]:
        print(element)
        break
    print(element,end= " ")