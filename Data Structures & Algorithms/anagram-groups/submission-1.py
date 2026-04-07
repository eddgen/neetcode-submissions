class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            letter_occurence = [0]*26
            for char in string:
                letter_occurence[ord(char)-ord('a')] +=1
        
            res[tuple(letter_occurence)].append(string)

        return list(res.values())