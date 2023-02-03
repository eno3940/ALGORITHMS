import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n= int(input())
m = int(input())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1,m+1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True)-1)