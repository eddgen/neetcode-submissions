class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq={}
        if not nums:
            return 0
        
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        longest=1
        sequence=0

        for num in range(min(nums),max(nums)+1):
            if freq.get(num,0)==0:
                if sequence>longest:
                    longest=sequence
                sequence=0
            else:
                sequence+=1
        
        if sequence>longest:
            longest=sequence
        return longest