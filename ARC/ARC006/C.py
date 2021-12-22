# n = int(input())
# list_box = []
# stack_li = [[-1] for i in range(n)]
# for i in range(n):
#     w = int(input())
#     list_box.append(w)
# max_idx = n
# remove_idx = []
# for i in range(n):
#     max_idx = list_box.index(max(list_box[:max_idx]))
#     stack_li[i] = [list_box[max_idx]]
#     tmp = max_idx
#     remove_idx.append(tmp)
#     if tmp == 0:break
# remove_idx.sort(reverse=True)
# for i in remove_idx:
#     list_box.remove(list_box[i])
# last_row = -1
# for j in range(len(list_box)):
#     cnt = 10000000
#     for k in range(len(stack_li)):
#         if list_box[j] <= stack_li[k][-1]:
#             subtraction = stack_li[k][-1] - list_box[j]
#             cnt = min(cnt,subtraction)
#             if cnt == subtraction:
#                 add_idx = k
#     if cnt == 10000000:
#         stack_li[last_row].append(list_box[j])
#         stack_li[last_row].remove(-1)
#         last_row -= 1
#     else:
#         stack_li[add_idx].append(list_box[j])
# ans = 0
# for i in stack_li:
#     if i[0] == -1:
#         ans += 1
# if ans == 0:
#     print(n)
# else:
#     print(len(stack_li)-ans)
                


N = int(input())
W = [int(input()) for _ in range(N)]
W.reverse()
mountain = [W[0]]

for i in range(1, N):
    mountain = sorted(mountain, reverse=True)
    judge = False
    for j in range(len(mountain)):
        if W[i] >= mountain[j]:
            mountain[j] = W[i]
            judge = True
            break
    if not(judge):
        mountain.append(W[i])
print(len(mountain))


