number_N = input()
N = list(number_N)
length = len(N)
ans = 0
if length % 2 == 1:
    ans = 10**((length-1)//2)-1
else:
    for i in range(length//2):
        if i == length//2 -1:
            cnt = int(number_N[0:length//2])-ans
            if int(number_N[0:length//2]) > int(number_N[length//2:]):
                cnt -= 1
            ans += cnt
        else:
            ans = 10  * ans + 9 
print(ans)