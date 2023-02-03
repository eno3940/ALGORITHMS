import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(1,n):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
parents = [0]*(n+1)

def dfs(start):
    for i in tree[start]:
        if parents[i]==0:
            parents[i]=start
            dfs(i)

dfs(1)
for i in range(2,n+1):
    print(parents[i], end='\n')
