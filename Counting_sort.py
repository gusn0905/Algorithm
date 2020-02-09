# 카운팅 정렬
def Counting_Sort(unsorted_list, sorted_list, k):
    # unsorted_list[1.....n] 초기에 정렬되지 않은 리스트
    # sorted_list[1....n] 정렬된 리스트, unsorted와 길이 맞춰서 초기화
    # cnt_list[1....n] 카운트 리스트

    cnt_list = [0] * k

    for i in range(0, len(sorted_list)):
        cnt_list[unsorted_list[i]] += 1

    for i in range(1, len(cnt_list)):
        cnt_list[i] += cnt_list[i - 1]

    for i in range(len(sorted_list)-1, -1, -1):
        sorted_list[cnt_list[unsorted_list[i]]-1] = unsorted_list[i]
        cnt_list[unsorted_list[i]] -= 1

    return sorted_list

a = [0,4,1,3,1,2,4,1]
b = [0] * len(a)
print(Counting_Sort(a,b,max(a)+1))
# cnt_list = [0,0,0,0,0]
# cnt_list = [1,4,5,6,8]
# sorted_list[cnt_list[1]-1] = sorted_list[3] = 1, cnt_list = [1,3,5,6,8] , sorted_list = [0,0,0,1,0,0,0,0]
# sorted_list[cnt_list[4]-1] = sorted_list[7] = 4, cnt_list = [1,3,5,6,7] , sorted_list = [0,0,0,1,0,0,0,4]
# sorted_list[cnt_list[2]-1] = sorted_list[4] = 2, cnt_list = [1,3,4,6,7] , sorted_list = [0,0,0,1,2,0,0,4]
# sorted_list[cnt_list[1]-1] = sorted_list[2] = 1, cnt_list = [1,2,4,6,7] , sorted_list = [0,0,1,1,2,0,0,4]
# sorted_list[cnt_list[3]-1] = sorted_list[5] = 3, cnt_list = [1,2,4,5,7] , sorted_list = [0,0,1,1,2,3,0,4]
# sorted_list[cnt_list[1]-1] = sorted_list[1] = 1, cnt_list = [1,1,4,6,7] , sorted_list = [0,1,1,1,2,3,0,4]
# sorted_list[cnt_list[4]-1] = sorted_list[6] = 4, cnt_list = [1,1,4,6,6] , sorted_list = [0,1,1,1,2,3,4,4]
# sorted_list[cnt_list[0]-1] = sorted_list[0] = 0, cnt_list = [0,1,4,6,7] , sorted_list = [0,1,1,1,2,3,4,4]
