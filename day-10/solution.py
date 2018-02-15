n = int(input().strip())

current_consecutive_1s = 0
max_consecutive_1s = 0
while n > 0:
    remainder = n % 2
    n = n // 2
    if remainder == 1:
        current_consecutive_1s += 1
        if current_consecutive_1s > max_consecutive_1s:
            max_consecutive_1s = current_consecutive_1s
    else:
        current_consecutive_1s = 0

print(max_consecutive_1s)
