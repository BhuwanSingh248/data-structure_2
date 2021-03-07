# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]


def mergedSortedArray(nums1, nums2):
    start = 0
    n = len(nums1)
    m = len(nums2)
    for i in range(nums1):
        if 

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,7]
print(mergedSortedArray(nums1, nums2))
    
