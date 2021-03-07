def findMaxSum(arr):
    sum = -100
    for i in arr:
        sum = max(sum+i, sum)
    return sum
print(findMaxSum([1,-2,3]))