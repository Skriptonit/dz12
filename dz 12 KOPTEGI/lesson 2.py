# Функция slicer() на вход принимает кортеж и случайный элемент.
# Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем
# и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, который начинается с него
# и идет до конца исходного.

def slicer(kor,elem):
    n = tuple ()
    m = (kor.count (elem))
    if m ==0:
        return n
    elif m==1:
       return kor[kor.index(elem):]
    elif m >1 :
        f_index = kor.index(elem)
        s_index = kor.index(elem, f_index + 1) + 1
        return kor [f_index:s_index]


print("Введите последовательность чисел : ")
a = [float(i) for i in input().split()]
kor = tuple(a)

print ("Введите элемент :")
elem = float (input())
print (slicer(kor,elem))