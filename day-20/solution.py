n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0
for i in range(n):
    currentSwaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            numSwaps += 1
            currentSwaps += 1

    if currentSwaps == 0:
        break

print('Array is sorted in ' + str(numSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))
