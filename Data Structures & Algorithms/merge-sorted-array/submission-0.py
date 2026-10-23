# def mergeSort(List[] arr, int s, int e):
#     if(e - s + 1 <= 1)
#         return arr
    
#     m = (s+e) / 2
#     mergeSort(arr, s, m)
#     mergSort(arr, m+1, e)

#     print(arr)

#     return arr


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        
        nums1[m:] = nums2[:]
        
        # print(nums1)

        # nums1 = mergeSort(nums1, 0, m+n)

        nums1.sort()