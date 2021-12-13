import sys
#再起上限を増やす
sys.setrecursionlimit(1000000)
def dfs(x,y):
    if x<0 or y<0 or x>=w or y >= h: return
    if field[y][x] =="#": return
    if field[y][x] == "g":
        print("Yes")
        sys.exit()
    if seen[y][x]:return
    seen[y][x] = True

    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)

h,w = map(int,input().split())
field = [list(input()) for _ in range(h)]
seen =  [[False]*(w) for i in range(h)]

for i in range(w):
    for j in range(h):
        if field[j][i] == "s":
            sh = j
            sw = i
        if field[j][i] == "g":
            gh = j
            gw = i
dfs(sw,sh)
print("Yes" if seen[gh][gw] else "No")
   

