import sys
path = __file__[0:-2] + 'txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

n,x = map(int,input().split())
array = list(map(int, input().split()))

from bisect import bisect_left,bisect_right

def count_by_range(array,left_value,right_value):
    left_index=bisect_left(array,left_value)
    right_index=bisect_right(array,right_value)
    return right_index-left_index

print(count_by_range(array,x,x))