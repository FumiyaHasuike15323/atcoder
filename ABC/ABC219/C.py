x = input()
n = int(input())
field = []
ans_li = []
for i in range(n):
    s = input()
    ans_li.append(s)
    cnt = ""
    for j in range(len(s)):
        letter = chr(x.index(s[j])+97)
        cnt += letter
        
    field.append([cnt,i])
field.sort()
for i in range(n):
    print(ans_li[field[i][1]])
