import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
num_list=[]
a = int(input())
for i in range(a):
    num_list.append(int(input()))
num_list.sort()
for num in num_list:
    print(num)
