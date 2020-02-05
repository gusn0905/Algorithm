# 버블 정렬
sample = [55, 7, 78, 12, 42, 33, 47, 12, 86, 36, 85, 66, 45]
def BubbleSort(a): # 정렬할 List
    for i in range(len(a)-1, 0, -1) : # 범위의 끝 위치, 헷갈릴때 범위 그냥 n으로 해도 됨
        for j in range(0, i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(BubbleSort(sample))