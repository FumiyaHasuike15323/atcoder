s = input()
t = input()
ans = ["a"]*len(s)
flag = 0
point_same = -1
t_letter_cnt = len(t)
for i in range(len(s)-len(t)+1):
    flag = 0
    for j in range(1,t_letter_cnt+1):
        if s[-(i+j)] == t[-j] or s[-(i+j)] == "?":
            continue
        else:
            flag = 1
    if flag == 0:
        point_same = i
        break
if point_same == -1:
    print("UNRESTORABLE")
    exit()
for i in range(1,len(s)+1):
    if s[-i] == "?":
        ans[-i] = "a"
    else:
        ans[-i] = s[-i]
for i in range(1,len(t)+1):
    ans[-(point_same+i)] = t[-i]
for i in range(len(s)):
    print(ans[i],end="")

