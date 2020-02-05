# 2020.02.03 연습문제2
arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
cnt = 0
sum_list = []
for i in range(1, 1<<n):
    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(arr[j])
    print(temp)
    sum_list.append(sum(temp))
cnt = sum_list.count(0)
print(cnt)