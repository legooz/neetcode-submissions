class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        subsets = []
        def dfs(i):
            if(i == len(nums)):
                answer.append(subsets.copy())                
                return

            subsets.append(nums[i]) # 1,2,3

            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)


        dfs(0)

        return answer