# 2020.02.04 선택 정렬
def SelectionSort(lst):
    for i in range(len(lst)-1):
        min = i
        for j in range(i+1,len(lst)):
            if lst[min] > lst[j]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst

ex = [64,25,10,22,11]
print(SelectionSort(ex))