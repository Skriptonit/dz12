# На вход функции sieve() поступает список целых чисел.
# В результате выполнения этой функции будет получен кортеж уникальных элементов списка в обратном порядке.

def sieve(kop):
    b = []
    for i in reversed(kop):
        if i not in b:
            b.append(i)
    return tuple(b)

print ("Введите последовательность чисел :")
a = [int (i) for i in input().split()]
kop = tuple(a)
print(sieve(kop))


