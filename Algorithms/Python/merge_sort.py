'''
Сортировка слиянием (Merge Sort)

Алгоритм:
1. Сортируемый массив разбивается на две части примерно одинакового размера.
2. Каждая из получившихся частей сортируется отдельно, например, тем же самым алгоритмом.
3. Два упорядоченных массива половинного размера соединяются в один.

В среднем время сортировки слиянием составляет O(n log n).

Преимущества: работает даже на структурах данных 
последовательного доступа, хорошо сочетается с подкачкой и кэшированием,
хорошо параллелится, не имеет «трудных» входных данных, устойчивая - сохраняет порядок равных элементов.

Недостатки: требуется дополнительная память, частичная отсортированность
никак не влият на скорость работы.
'''

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

arr = [1, 45, 9, 1, 5]
print(merge_sort(arr))