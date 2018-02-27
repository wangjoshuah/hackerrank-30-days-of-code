n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

reversed_array = []
for i in range(len(arr)):
    reversed_array.append(arr[n-i-1])

# print(' '.join(str(i) for i in reversed_array))

output_string = ''
for i in range(len(reversed_array)):
    output_string += str(reversed_array[i]) + ' '

print(output_string)
