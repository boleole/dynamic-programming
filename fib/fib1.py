def fib(number):
    if number <= 2:
        return 1
    result = fib(number -1) + fib(number -2)
    return result

tabell = {1: 1, 2: 1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1}

def fib_dyn(number):
    if number <= 2:
        return tabell[number]
    if tabell[number] == -1:
        tabell[number] = fib_dyn(number - 1) + fib_dyn(number - 2)
    return tabell[number]



print(str(fib(6)))
print(str(fib(7)))
print(str(fib(8)))

print(str(fib_dyn(8)))
print(tabell)
