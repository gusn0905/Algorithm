# 2020.02.04 이진검색 연습
def binarySearch(a,key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True # 검색 성공
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

ex = [6,3,15,75,98,33,64,68,42,61,79,46]
ex.sort()
print(binarySearch(ex,0))

# #재귀함수
def binarySearch2(a,low,high,key):
    if low > high: #검색 실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle] : #검색 성공
            return True
        elif key < a[middle] :
            return binarySearch2(a,low,middle-1,key)
        elif a[middle] < key:
            return binarySearch2(a,middle+1,high,key)
