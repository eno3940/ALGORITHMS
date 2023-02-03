array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return # return으로 함수를 빠져 나갈 수 있음
    pivot = start #시작 지점이 pivot, 기준
    left = start + 1 #pivot에서 오른쪽으로 한칸씩
    right = end #분할 된 구역에서의 마지막 부분
    while(left <= right): #교차 되기 전 까지 반복
        while(left <= end and array[left] <= array[pivot]): #피벗 값보다 작으면 오른쪽으로 한 칸씩 가서 탐색
            left+=1
        while(right >start and array[right] >= array[pivot]): #피벗 값보다 크면 왼쪽으로 한 칸씩 가서 탐색
            right -=1
        if(left >right): #탐색 결과 교차 되면 피벗값을 right기준(교차된 지점에서 더 작은 값)으로 스와프
            array[right], array[pivot] = array[pivot], array[right]
        else: #교차 되기 전 까지 작은 값(right)과 큰 값(left)을 스와프
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1) #교차 돼서 9번 줄 while에 벗어나면 분할 구역 기준으로 재귀
    quick_sort(array, right+1, end) # 오른쪽 분할 구역 다시 반복/재귀

quick_sort(array,0,len(array)-1)
print(array)
