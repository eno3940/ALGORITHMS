def letterfind(s,answer):
    if len(s)==0:
        return answer
    cnt=0
    other_cnt=0
    first_letter=s[0]
    for i in s:
        if i == first_letter:
            cnt+=1
        else:
            other_cnt+=1
        if cnt == other_cnt:
            break
    answer+=1
    s = s[cnt*2:]
    letterfind(s,answer)

def solution(s):
    letterfind(s)
    return answer

s = "aaabbaccccabba"
answer = 0
letterfind(s,answer)
