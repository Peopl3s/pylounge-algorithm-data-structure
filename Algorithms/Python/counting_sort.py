'''
Сортировка Подсчётом (Counting Sort)

Подсчитываем, сколько раз в массиве встречается каждое значение,
и заполняем массив подсчитанными элементами 
в соответствующих количествах. 
Счётчики для всего диапазона чисел создаются заранее 
(изначально равны нулю).

Является необменной сортировкой!

Сложность сортировки по времени
Худшая O(n + k)
Средняя O(n + k)
Лучшая O(n)

Преимущества:
1. Устойчивая
2. Применение сортировки подсчётом целесообразно лишь тогда, 
когда сортируемые числа имеют (или их можно отобразить в) 
диапазон возможных значений, который достаточно мал
по сравнению с сортируемым множеством.

Недостатки:
1. Эффективность алгоритма падает, если при попадании нескольких 
различных элементов в одну ячейку, их надо дополнительно сортировать.
2. Линейное время работы 

'''

def counting_sort(arr, max_element):
  c = [0] * (max_element + 1)
  for i in range(len(arr)):
    c[arr[i]] = c[arr[i]] + 1

  pos = 0
  for i in range(len(c)):
    for j in range(c[i]):
      arr[pos] = i
      pos +=1 
  return arr

l = [1, 5, 0, 99, 12, 6]
max_element = max(l)
print(counting_sort(l, max_element))