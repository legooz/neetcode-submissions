class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R: # target = 5
            M = (L + R) // 2 # [1, 2, 3 ,4] 
            print(M)
            if(target < nums[M]): # [(l)1, 2(m), 3 ,4(r)]
                R = M - 1 
            elif (target > nums[M]):
                L = M + 1 # [1, 2, (m)(l)3 ,4(r)]
            else:
                return nums.index(target)

        return -1