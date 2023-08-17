import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n,k = map(int,input().split())

area = [0]*200001 #input 최대가 100000, 곱하기2가 제일 크게 늘릴수 있으므로 200000+1

from collections import deque
queue=deque([n])
def bfs():
    while queue:
        x = queue.popleft()
        if x == k:
            print(area[x])
            break
        for i in [x+1,x-1,x*2]:
            if 0<=i<=200000 and not area[i]: #0이어야 queue에 넣음. 방문처리 안된 곳
                queue.append(i)
                area[i]=area[x]+1

bfs()
