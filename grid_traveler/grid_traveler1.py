def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


print(str(grid_traveler(1, 1)))
print(str(grid_traveler(2, 3)))
print(str(grid_traveler(3, 2)))
print(str(grid_traveler(3, 3)))
print(str(grid_traveler(16, 16)))
