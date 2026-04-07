class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        times_occured = {}

        for num in nums:
            times_occured[num] = times_occured.get(num,0)+1
        
        for i in range(k):
            most_occurence=max(times_occured,key=times_occured.get)
            res.append(most_occurence)
            times_occured.pop(most_occurence)

        return res