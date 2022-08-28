tabell = []

def fib_tab(number):
    # Setter verdier til 0 i tabellen først, deretter legger til 1 i
    # tabell[1], som startverdi
    for i in range(number):
        tabell.append(0)
    tabell[1] = 1
    for i in range(2, len(tabell), 1):
        tabell[i] = tabell[i -2 ] + tabell[i - 1]
    return tabell[number - 1]

print(str(fib_tab(50)))
print(str(len(tabell)))
print(tabell)