# 2D Lists & Nested Loops (2:47:13)

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# [COLUMN][ROW]
print(number_grid[0][1])


## Nested Loops
print("")
for num_list in number_grid:
    for num in num_list:
        print(num)