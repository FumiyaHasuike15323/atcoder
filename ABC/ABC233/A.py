x,y = map(int,input().split())
if x >= y:
    print(0)
else:
    print((y+9-x)//10)