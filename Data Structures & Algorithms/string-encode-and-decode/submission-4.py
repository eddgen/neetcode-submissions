class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=""
        for string in strs:
            encode+= str(len(string)) + "#" + string 
        
        return encode


    def decode(self, s: str) -> List[str]:
        decode=[]

        i=0

        while i < len(s):
            word=""
            length=""

            j = i
            while s[j] != "#":
                length+=s[j]
                j+=1

            int_length = int(length)
            i=j+1
            j=i+int_length

            word=s[i:j]
            decode.append(word)
            i=j

        return decode
