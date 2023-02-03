array = [7,5,9,0,3,1,6,2,4,8]

def ssort(array):
    for i in range(len(array)): #각 자리에 올 최솟값을 찾아서(선택) 스와프 해야하므로 len(array)만큼 반복
        min_index = i # 일단 시작하는 자리(index)를 가장 작은 원소로 잡고 제일 작은 원소 찾기
        for j in range(i+1, len(array)): #각 자리 이후에 원소들 중에서 제일 작은 원소 선형탐색
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index] #스와프
    return array

print(ssort(array))