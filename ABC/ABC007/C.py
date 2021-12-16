r,c = map(int,input().split())
sy,sx = [int(x) -1 for x in input().split()]
gy,gx = [int(x) -1 for x in input().split()]
Graph = [list(input())for i in range(r)]
visited= [[0]*c for _ in range(r)]

def bfs():
    queue = [[sy,sx,0]]
    while True:
        y,x,distance = queue.pop(0)
        if y == gy and x == gx:
            return distance
        for dy,dx in [[-1,0],[1,0],[0,-1],[0,1]]:
            ny = y+dy
            nx = x+dx
            if 0 <= nx < c and 0 <= y < r and visited[ny][nx] == 0 and Graph[ny][nx] == ".":
                visited[ny][nx] = 1
                queue.append([ny,nx,distance+1])

print(bfs())