tabell = []

def fib_tab(number):
    # Setter verdier til 0 i tabellen først, deretter legger til 1 i
    # tabell[1], som startverdi
    for i in range(number + 2):
        tabell.append(0)
    tabell[1] = 1
    for i in range(0, number, 1):
        tabell[i + 1] += tabell[i]
        tabell[i + 2] += tabell[i]
    return tabell[number]

print(str(fib_tab(8)))
print(str(len(tabell)))
print(tabell)
