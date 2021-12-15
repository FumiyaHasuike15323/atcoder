import sys
sys.setrecursionlimit(1000000000)

h,w = map(int,input().split())
field = [list(input()) for _ in range(h)]
que = []
visited = [[0]*w for _ in range(h)]
shape_cnt = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == "#":
            shape_cnt += 1


def bfs():
    que.append([0,0,0])
    while que != []:
        y,x,distance = que.pop(0)
        if y == h-1 and x == w-1:
            cnt = distance
            ans = h*w - (cnt+1) - shape_cnt
            print(ans)
            exit()
        for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == 0 and field[ny][nx] == ".":
                visited[ny][nx] = 1
                que.append([ny,nx,distance+1])
    print(-1)

bfs()