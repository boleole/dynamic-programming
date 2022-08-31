tabell = []

def grid_traveler(m, n):
    for i in range(m + 1):
        tabell.append([])
        for j in range(n + 1):
            tabell[i].append(0)
    tabell[1][1] = 1
    for i in range(len(tabell)):
        if i != len(tabell) - 1:
            for j in range(0, len(tabell[i]), 1):
                if tabell[i][j] != 0 and j != len(tabell) - 1:
                    tabell[i][j + 1] += tabell[i][j]
                    tabell[i + 1][j] += tabell[i][j]
                elif tabell[i][j] != 0 and j == len(tabell) - 1:
                    tabell[i + 1][j] += tabell[i][j]
        else:
            for j in range(0, len(tabell[i]), 1):
                if tabell[i][j] != 0 and j != len(tabell) - 1:
                    tabell[i][j + 1] += tabell[i][j]
            return tabell[i][j]
        



print(str(grid_traveler(3,3)))
print(tabell)
