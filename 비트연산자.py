# 2020.02.03 비트 연산자
arr = [3,6,7]
n = len(arr)
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()
print()
