array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array,start,end):
    if start>=end:
        return
    pivot = start
    left = start +1
    right = end
    #교차 될 때 까지 반복
    while (left<=right):
        #왼쪽에서 부터 pivot값 보다 큰 값을 찾을 때 까지 반복
        #왼쪽에서 부터 시작해서 end값보다 넘어가면 안되므로 조건 설정(indexError 유발할 수 있음)
        while (left <= end and array[left] <= array[pivot]):
            left +=1
        #오른쪽에서 부터 pivot값 보다 작은 값을 찾을 때 까지 반복
        #right와 start(pivot)이 같아지거나 right가 더 작아지면(right<=start(pivot)) 역시 indexError
            #start값은 첫번째 원소이기 때문에, 그리고 같아지는 경우에는 right와 pivot을 바꾸는데 아무의미X
        while (right>start and array[right] >= array[pivot]):
            right -=1
        #교차하면 right(작은값)과 pivot값을 바꿈
        if (left>right): #left>=right로 하면 안됨!!!
            array[pivot],array[right] = array[right], array[pivot]
        #교차하지 않으면 right와 left값을 바꿈
        else:
            array[right],array[left] = array[left], array[right]
    #재귀로 나눠진 부분 끼리 반복
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array, 0, len(array)-1)
print(array)