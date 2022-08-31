tabell = {}

def grid_traveler(m, n):
    # are the args in tabell
    key = str(m) + "," + str(n)
    if key in tabell:
        return tabell[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    if key not in tabell:
        tabell[key] = grid_traveler(m - 1, n) + grid_traveler(m, n - 1)
    return tabell[key]


print(str(grid_traveler(1, 1)))
print(str(grid_traveler(2, 3)))
print(str(grid_traveler(3, 2)))
print(str(grid_traveler(3, 3)))
print(str(grid_traveler(5, 5)))
print(tabell)
print(str(grid_traveler(18, 18)))
