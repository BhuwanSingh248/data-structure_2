def stockMerch(arr):
    from collections import Counter
    a = Counter(arr)
    count = 0
    for i in a.values():
        count += i//2
    return count

stockMerch([10,20,20,10,30,10,50,10,20])