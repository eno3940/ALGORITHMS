def solution(numbers):
    from collections import deque
    result = deque()
    numbers = deque(numbers)
    s = deque()
    i = 0
    while True:
        s = numbers.popleft()
        if numbers ==deque([]):
            result.append(-1)
            break
        while s >= numbers[i] : #s보다 큰 수 나오면 stop
            i += 1
            if i == len(numbers):
                result.append(-1)
                break
        try:
            result.append(numbers[i])
        except:
            pass
        i = 0
    return result

numbers = [9, 1, 5, 3, 6, 2]
print(solution((numbers)))