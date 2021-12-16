
import sys
import collections
import copy
sys.setrecursionlimit(1000000000)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check(tmp):
    for i in range(10):
        for j in range(10):
            if tmp[i][j] == "o":
                return False
    return True

def dfs(x,y,tmp):
    tmp[x][y] = "x"
    for p in range(4):
        nx = x + dx[p]
        ny = y + dy[p]
        if (0 <= nx < 10) and (0 <= ny < 10) and tmp[nx][ny] =="o":
            dfs(nx,ny,tmp)

field = [list(input()) for i in range(10)]
for i in range(10):
    for j in range(10):
        tmp = copy.deepcopy(field)
        if tmp[i][j] == "x":
            dfs(i,j,tmp)
            if check(tmp):
                print("YES")
                exit()
print("NO")