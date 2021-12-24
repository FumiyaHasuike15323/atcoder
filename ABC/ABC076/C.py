s_ = input()
t = input()
sl = len(s_)
tl = len(t)
s = []
a = s_.replace("?", "a")

for i in range(sl-tl+1):
  tmp = s_[i:i+tl]
  for j in range(tl):
    if tmp[j] == "?": continue
    if tmp[j] != t[j]: break
  else:
    s.append(a[:i] + t + a[tl+i:])

s.sort()
if len(s) != 0:
  print(s[0])
else:
  print("UNRESTORABLE")