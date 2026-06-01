class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_remove = []

        for i in range(len(nums)-1):
            if(nums[i] == nums[i + 1]):
                to_remove.append(i)


        to_remove = to_remove[::-1]


        for i in sorted(to_remove, reverse=True):
            nums.pop(i)

        k = len(nums)          

        return k