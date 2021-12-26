l,r = map(int,input().split())
l -= 1
r -= 1
s = input()
reverse_s = "".join(list(reversed(s[l:r+1])))
print(s[:l]+reverse_s+s[r+1:])

