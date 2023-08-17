def solution(citations):
    citations.sort()
    cnt=0
    num_pop=0
    while citations:
        h = citations.pop()
        num_pop+=1
        if h<=num_pop:
            return max(h,(num_pop-1))
    return num_pop