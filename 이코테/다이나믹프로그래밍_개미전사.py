import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

d= [0]*n
d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    d[i] = max((d[i-2]+array[i]),(d[i-1]))
print(d[n-1])