class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        subsets = []
        # 6 4 = 12

        def dfs(i, remaining):

            if remaining < 0 or i >= len(nums):
                return

            if remaining == 0:
                answer.append(subsets.copy())
                return

            subsets.append(nums[i])
            
           

            dfs(i, remaining - nums[i]) 
            subsets.pop()

            dfs(i + 1, remaining)


            
        dfs(0, target)

        return answer