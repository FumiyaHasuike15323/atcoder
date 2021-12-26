N,M = map(int,input().split())
janken = []
for j in range(2*N):
    a = list(input())
    a = [0 if i == "G" else i for i in a]
    a = [1 if i == "C" else i for i in a]
    a = [2 if i == "P" else i for i in a]
    a.append(j) #番号
    a.append(100) #勝利したらカウント減る
    janken.append(a)

for i in range(M):
    for j in range(0,2*N,2):
        if (janken[j][i] - janken[j+1][i]+3)% 3 == 1:
            janken[j+1][-1] -= 1
        elif (janken[j][i] - janken[j+1][i]+3)% 3 == 0:
            continue
        else:
            janken[j][-1] -= 1
    janken = sorted(janken, key=lambda x:(x[-1], x[-2]))
for i in range(2*N):
    print(janken[i][-2]+1)

