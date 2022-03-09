
def workbook(n, k, arr):
    page_num = 1
    spc_prob = 0
    for total_prob in arr:
        for i in range(1, total_prob+1, k):
            print(range(i,i+k if i+k <= total_prob+1 else i + (total_prob%k)), 'page_num=',page_num)
            if page_num in range(i,i+k if i+k <= total_prob+1 else i + (total_prob%k)):
                print("hi")
                spc_prob += 1
            page_num += 1

    return spc_prob



print(workbook(5, 3, [4,2,6,1,10]))
#
# for i in range(1,4,3):
#     print(i)