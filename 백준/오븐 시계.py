import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
h,m = input().split()
add_m=int(input())
print(add_m+m)