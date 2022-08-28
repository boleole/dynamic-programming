tabell = {}

def fib_dyn(number):
    if number in tabell:
        return tabell[number]
    if number <= 2:
        return 1
    if number not in tabell:
        tabell[number] = fib_dyn(number - 1) + fib_dyn(number - 2)
    return tabell[number]


print(str(fib_dyn(50)))
print(str(len(tabell)))
