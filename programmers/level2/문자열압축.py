def get_compressed(s, chunk_size):
    compressed = 0
    chunk = s[:chunk_size]
    repeat_count = 1
    
    for offset in range(chunk_size, len(s) + 1, chunk_size):
        compare = s[offset:offset+chunk_size]

        if chunk == compare:
            repeat_count += 1
        else :
            if repeat_count == 1:
                compressed += len(chunk)
            else:
                compressed += len(f"{repeat_count}{chunk}")
            
            chunk = compare
            repeat_count = 1
    compressed += len(chunk)

    return compressed


def solution(s):
    answer = len(s)  # 압축률 0% 최대 길이

    # 1글자 ~ 문자열의 절반만큼 압축을 해봄.. 자르는 길이가 문자열 길이의 절반을 넘기면 압축이 되지 않음
    for chunk_size in range(1, len(s) // 2 + 1):
        compressed_size = get_compressed(s, chunk_size)
        answer = min(answer, compressed_size)

    return answer

s = "abcabcabcabcdededededede"
print(solution(s))