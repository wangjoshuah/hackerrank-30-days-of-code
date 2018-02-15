grid = list()

for i in range(6):
    row = input().strip().split(' ')
    row = list(map(int, row))
    grid.append(row)

def _get_hourglass_sum(grid, i, j):
    sum = 0
    sum += grid[i-1][j-1]
    sum += grid[i-1][j]
    sum += grid[i-1][j+1]
    sum += grid[i][j]
    sum += grid[i+1][j-1]
    sum += grid[i+1][j]
    sum += grid[i+1][j+1]
    return sum

# start max_hourglass_sum at smallest possible hourglass
max_hourglass_sum = -63
for i in range(1,5):
    for j in range(1, 5):
        current_hourglass_sum = _get_hourglass_sum(grid, i, j)
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum = current_hourglass_sum

print(max_hourglass_sum)
