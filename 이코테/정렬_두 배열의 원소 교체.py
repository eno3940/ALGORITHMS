import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i], a[i]
    else:
        break
print(sum(a))