# wrong

def removeKdigit(nums, k):
    result = []
    temp = -1
    for i in nums:
        print(i)
        while i < temp and k>0 and len(result) != 0:
            print("1111111111111111111111")
            result.pop()
            k -= 1
        if len(result) != 0 or i != 0:
            print("22222222222222222222")
            result.append(i)
            temp = i
    
    while len(result) != 0 and k > 0:
        print("::::")
        result.pop()
        k -= 1
    if len(result) == 0:
        print("LLLLLL")
        return 0
    return result

print(removeKdigit([1,4,5,3,4,8], 3))



