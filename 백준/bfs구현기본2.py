# 0. 입력 및 초기화
import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N+1)]
visited = [False] * (N+1)

# 1. graph 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

from collections import deque
q = [1]
def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N +1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
bfs()