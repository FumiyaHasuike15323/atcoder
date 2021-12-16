charge = 1000 - int(input())
cnt_coin = 0
coin_kind = [500,100,50,10,5,1]
for i in range(6):
    t = charge // coin_kind[i]
    charge -= t*coin_kind[i]
    cnt_coin += t
print(cnt_coin)