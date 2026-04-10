class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]

        prefix=[]

        suffix=[]
        curentPrefix=1
        prefix.append(1)
        for num in nums:
            curentPrefix *= num
            prefix.append(curentPrefix)
        
        prefix.pop()

        curentSuffix=1
        suffix.append(1)
        for num in nums[::-1]:
            curentSuffix*=num
            suffix.append(curentSuffix)
        
        suffix.pop()

        for i in range(len(nums)):
            output.append(suffix[len(nums)-1-i]*prefix[i])

        print(prefix)
        print(suffix)
        return output