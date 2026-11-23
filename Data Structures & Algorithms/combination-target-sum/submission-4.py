class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        subsets = []

        
        def dfs(i, remaining):
            
            if i >= len(nums) or remaining < 0 :
                return

            if remaining == 0 and subsets not in answer:
                answer.append(subsets.copy())
                return

            subsets.append(nums[i])
            
            dfs(i, remaining - nums[i])
            
        

            subsets.pop()

            
            dfs(i+1, remaining)

        dfs(0, target)


        return answer