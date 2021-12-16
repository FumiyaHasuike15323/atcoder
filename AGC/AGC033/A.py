from collections import deque
h,w = map(int,input().split())
field = [list(input())for _ in range(h)]
visited = [[-1]*w for _ in range(h)]
que = deque([])
ans = 0

for i in range(h):
    for j in range(w):
        if field[i][j] == "#":
            que.append((i,j))
            visited[i][j] = 0

def bfs():
    global ans
    while que:
        y,x = que.popleft()
        for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
            ny = y+dy
            nx = x+dx
            if 0 <= nx < w and 0<= ny < h:
                t = visited[y][x]
                if visited[ny][nx] != -1:continue
                visited[ny][nx] = t+1
                que.append((ny,nx))
                ans = max(ans,t+1)

bfs()
print(ans)