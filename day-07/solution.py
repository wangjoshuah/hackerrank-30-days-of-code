n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.reverse()

print(' '.join(str(i) for i in arr))
