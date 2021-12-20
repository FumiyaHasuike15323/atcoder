from collections import deque
import sys
sys.setrecursionlimit(100000000)
h,w = map(int,input().split())
field = [list(input()) for _ in range(h)]
visited = [[0]*w for i in range(h)]
que = deque([])
que.append([0,0,0])
ans = 0
def bfs():
    global ans
    while que:
        y,x,distance = que.popleft()
        for dy,dx in [[1,0],[0,1]]:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < h and 0<= nx < w :
                if field[ny][nx] == "." and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    cnt = distance+1
                    que.append([ny,nx,cnt])
                    ans = max(ans,cnt)
bfs()
print(ans+1)
