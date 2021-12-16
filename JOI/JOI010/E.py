import sys
sys.setrecursionlimit(1000000000)

h,w,n = map(int,input().split())
field = [list(input())for _ in range(h)]
visited = [[0]*w for _ in range(h)]



que = []
distance = 0
for i in range(w):
    for j in range(h):
        if field[j][i] == "S":
            sw,sh = i,j
que.append([sh,sw,distance])
cnt = 1
ans = 0

def bfs():
    global que,cnt,ans,visited
    while True:
        y,x,distance = que.pop(0)
        if field[y][x] == str(cnt):
            if cnt == n:
                ans += distance
                print(ans)
                exit()
            cnt += 1
            ans += distance
            distance = 0
            visited = [[0]*w for _ in range(h)]
            que = [[y,x,0]]
        for dy,dx in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny = y+dy
            nx = x+dx
            if 0 <= nx < w and 0 <= ny < h and field[ny][nx] != "X" and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                que.append([ny,nx,distance+1])

bfs()
