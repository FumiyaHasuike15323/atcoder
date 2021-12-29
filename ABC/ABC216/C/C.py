n = int(input())
ans_li = []
for i in range(n):
    if n == 1:
        ans_li.append("A")
        break
    if n % 2 == 1:
        n -= 1
        ans_li.append("A")
    else:
        n //= 2
        ans_li.append("B")
for i in reversed(ans_li):
    print(i,end="")
