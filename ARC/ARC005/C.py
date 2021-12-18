from collections import deque
import sys
sys.setrecursionlimit(10000000)
h,w = map(int,input().split())
field = [list(input())for _ in range(h)]
visited = [[-1]*w for _ in range(h)]


for i in range(h):
    for j in range(w):
        if field[i][j] == "s":
            sh,sw = i,j
        elif field[i][j] == "g":
            gh,gw = i,j
que = deque([])
que.append([sh,sw])
visited[sh][sw] = 0
cnt = 0
def bfs():
    global cnt
    while que:
        y,x = que.popleft()
        for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < h and 0 <= nx < w and field[ny][nx] == "#" and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                que.append([ny,nx])
            elif 0 <= ny < h and 0 <= nx < w and field[ny][nx] == "." and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x]
                que.appendleft([ny,nx])
            elif 0 <= ny < h and 0 <= nx < w and field[ny][nx] == "g" and visited[ny][nx] == -1:
                if visited[y][x] <= 2:
                    print('YES')    
                    exit()
                break
            
bfs()
print('NO')