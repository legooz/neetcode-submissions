class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = set()
        answer = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pair = (nums[i], nums[j])
                if(nums[i] + nums[j] == target):
                    if pair not in seen:
                        print(pair)
                        seen.add(pair)
                        pair = (nums[j], nums[i])
                        seen.add(pair)

                        answer.append(i)
                        answer.append(j)         
        
        print(seen)
                    

        return answer