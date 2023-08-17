import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

len_array,target= map(int, input().split())
array=input().split()

end=max(array)
start=0
result=0
while (start<=end):
    mid=(start+end)//2
    total=0
    for x in array:
        if x > mid:
            total+=x-mid
    if total >target:
        start=mid+1
    elif total<=target:
        result=mid
        end=mid-1