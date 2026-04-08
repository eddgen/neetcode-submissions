class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        freq_buckets =[[] for _ in range(len(nums)+1)]

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        for num,freq in freq.items():
            freq_buckets[freq].append(num)

        for i in range (len(nums),0,-1):
            for j in range(len(freq_buckets[i])):
                res.append(freq_buckets[i].pop())
                if len(res)==k:
                    return res
