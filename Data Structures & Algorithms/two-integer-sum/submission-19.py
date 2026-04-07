class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        passed_by={}

        for i, num in enumerate(nums):
            nr1 = target - num
            
            if nr1 in passed_by:
                return [passed_by[nr1],i]

            passed_by[num]=i