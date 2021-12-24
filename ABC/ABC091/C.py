n = int(input())
red_coordinate,bule_coordinate = [],[]
for i in range(n):
    a,b = map(int,input().split())
    red_coordinate.append([a,b,0])
for i in range(n):
    a,b = map(int,input().split())
    bule_coordinate.append([a,b])
red_coordinate= sorted(red_coordinate, reverse= True, key=lambda x :x[1])
bule_coordinate.sort()
cnt = 0

for x,y in bule_coordinate:
    for j in range(len(red_coordinate)):
        if x > red_coordinate[j][0] and y > red_coordinate[j][1] and red_coordinate[j][2] == 0:
            cnt += 1
            red_coordinate[j][2] = 1
            break
print(cnt)
