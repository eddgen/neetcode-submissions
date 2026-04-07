class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            num2 = target - num

            if num2 == num:
                index1=nums.index(num)
                nums_copy=nums.copy()
                nums_copy.remove(num)
                if num2 in nums_copy:
                    index2=nums_copy.index(num2)+1
                    return [index1,index2]
                continue
            
            if num2 in nums:
                return [nums.index(num),nums.index(num2)]
