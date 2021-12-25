import bisect
n,k = map(int,input().split())
point = []
for i in range(n):
    p1,p2,p3 = map(int,input().split())
    sum = p1+p2+p3
    point.append(sum)
ranking_point = sorted(point,reverse =True)[k-1]
for i in range(n):
    print('Yes' if point[i]+300 >= ranking_point else 'No')