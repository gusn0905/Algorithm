# 2020.02.04 셀렉션 알고리즘
def select(lst,k):
    for i in range(k):
        minidx = i
        for j in range(i+1,len(lst)):
            if lst[minidx > lst[j]]:
                minidx = j
        lst[i], lst[minidx] = lst[minidx], lst[i]
    return lst[k-1]