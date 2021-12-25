n,a,b = map(int,input().split())
a -= 1
b -= 1
p,q,r,s = map(int,input().split())
p -= 1
q -= 1
r -= 1
s -= 1

for i in range(p,q+1):
    for j in range(r,s+1):
        if i+j == a+b or i-j == a-b:
            print("#",end = "")
        else:
            print(".",end="")
    print()

