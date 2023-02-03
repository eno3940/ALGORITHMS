import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]
from collections import deque
Q=deque([V])
for i in range(1,M+1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
visited_dfs=[False]*(N+1)
visited_bfs=[False]*(N+1)
def dfs(start):
    if start==V:
        print(start, end=" ")
    for a in graph[start]:
        if not visited_dfs[a]:
            visited_dfs[a]=True
            print(a, end=" ")
            dfs(a)
visited_dfs[V]=True
def bfs(start):
    visited_bfs[start]=True
    while Q:
        v = Q.popleft()
        print(v, end=" ")
        for a in graph[v]:
            if not visited_bfs[a]:
                Q.append(a)
                visited_bfs[a]=True
    
dfs(V)
print("")
bfs(V)
