# 오름차순으로 정렬
# while n!=0
# 두번째로 큰 수의 index를 찾는다
# 그전 인덱스까지의 수를 하나씩 뺀다 (두번째로 큰 수와 같을 떄 까지)
works=[4, 3, 3]
n = 4
def solution(n, works):
    works.sort(reverse=True) #오름차순 정렬
    answer = 0
    for __ in range(n): #n이 0이 되면 종료
        if works[0]==works[-1] and n!=0:
            temp=0
            for i in range(len(works)):
                temp+=works[i]
                works[i]-=1
                n-=1
                if n==0:
                    break
            if n >=temp:
                return 0
        if n==0:
            break
        for idx,work in enumerate(works): #두 번째로 큰 수의 index찾는 과정
            if works[0]>work:
                sec_idx=idx #두 번쨰로 큰 수의 index 저장
                break
            if works[0]==works[len(works)-1]:
                sec_idx= len(works)-1
                break
        while works[sec_idx-1]!=works[sec_idx] and n!=0:
            for i in range(0,sec_idx): #sec_index전까지 숫자 하나씩 뺌
                works[i]-=1
                n-=1
                if n==0:
                    break
    for i in range(len(works)):
        answer += works[i]*works[i]
    return answer
print(solution(n,works))