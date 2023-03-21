# Напишите функцию tpl_sort(), которая сортирует кортеж, состоящий из целых чисел по возрастанию и
# возвращает его.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.


def tpl_sort(n):
    for i in n:
        if not isinstance(i, float):
            return n
        else:
            return tuple(sorted(n))

print ("Введите последовательность чисел :")
a = [float (i) for i in input().split()]
n = tuple(a)
print(tpl_sort(n))