
def combinationUtil(arr, data , start, end , index = 0):
    if index == 2:
        global_arr.append([data[0], data[1]])
        return
    i = start
    while i<=end and end-i+1 >= 2-index:
        data[index] = arr[i]
        combinationUtil(arr, data, i+1, end, index+1)
        i+=1
# def callcomb(arr):
#     n = len(arr)
#     data = [0, 0]
#     combinationUtil(arr, data, 0, n-1, 0)

def combinationUtil2(arr):
    for i in arr:
        for j in arr:
            global_arr.append([i,j])
if __name__ == "__main__":
    import datetime
    arr = [i for i in range(9000)]
    global_arr = []
    a = datetime.datetime.now()
    combinationUtil(arr, [0]*2, 0, len(arr)-1)
    # combinationUtil2(arr)
    print(datetime.datetime.now() - a)
    # print(global_arr)
