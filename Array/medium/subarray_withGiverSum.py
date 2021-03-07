def reqArray(arr, s):
    l = 0
    ls = 0
    for i in range(len(arr)):
        ls += arr[i]
        while ls > s:
            ls -= arr[l]
            l += 1
        if ls == s:
            return (l, i)
    return -1


if __name__ == "__main__":
    arr = [1, 4, 20, 10, 3, 7]
    s = 33

    i, j = reqArray(arr, s)
    print(arr[j])
    print(arr[i:j+1])
