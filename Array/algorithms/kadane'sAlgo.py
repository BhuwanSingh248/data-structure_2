if __name__ == "__main__":
    arr = [-2, 4, -1, 2, 5, -6, 11, -11, 6]
    max_sum = arr[0]
    curr_sum = max_sum
    p1, p2 = 0, 0
    for i in range(1, len(arr)):
        if arr[i]+curr_sum > arr[i]:
            curr_sum = curr_sum+arr[i]
            print("in 1 : ", i)
        elif arr[i] > arr[i] + curr_sum:
            if arr[i] > curr_sum:
                p1 = i
            curr_sum=arr[i]
            print("in 2 : ", i)
        if curr_sum > max_sum:
            p2 = i
            max_sum = curr_sum
            print("in 3 : ", i)
        else:
            print("in 4 : ", i)
    print(max_sum,  "with pointer : ", p1, "and ", p2)