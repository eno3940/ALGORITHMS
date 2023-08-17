dungeons= [[20, 80], [80, 20], [50, 40], [30, 10]]
k = 80

from collections import deque

def solution(k, dungeons):
    answer = -1
    queue = deque()
    queue.append((k, [])) # 아무 곳도 안가는 경우의 수 추가
    while queue:
        x, visited_area= queue.popleft()
        for i in range(len(dungeons)):
            if x>= dungeons[i][0] and not [i] in visited_area:
                queue.append((k-dungeons[i][1], visited_area+[i]))
            else:
                answer = max(answer,len(visited_area))
    return answer

print(solution(k, dungeons))