class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary1 = {}
        for letter in s:
            dictionary1[letter] = dictionary1.get(letter,1) +1

        dictionary2 = {}
        for letter in t:
            dictionary2[letter] = dictionary2.get(letter,1) +1

        if dictionary1 == dictionary2:
            return True
        
        return False