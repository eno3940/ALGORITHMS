array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0 ,5, 2]

idx_array=[0]*(max(array)+1)

for i in range(len(array)):
    idx_array[array[i]] += 1
for i in range(len(idx_array)):
    for __ in range(idx_array[i]):
        print(i, end='')
