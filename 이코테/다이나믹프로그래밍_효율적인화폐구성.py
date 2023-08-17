import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

coin_num, target = map(int, input().split())
coins=[]
for i in range(coin_num):
    coins.append(int(input()))

d = [10001] * (target+1)

d[0] = 0
for i in range(coin_num):
    for j in range(coins[i], target+1):
        if d[j-coins[i]] != 10001:
            d[j] = min(d[j], d[j-coins[i]] + 1)

if d[target] == 10001:
    print(-1)
else:
    print(d[target])

