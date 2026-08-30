class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c = [0] * 16

        for i in range(len(s)):
            c[ord(s[i]) - ord('a')] += 1
            c[ord(s[i]) - ord('a')] -= 1
        
        for v in c:
            if v != 0:
                return False
        return True
        # charMap = {}
        # for c in s:
        #     charMap[c] = charMap.get(c, 0) + 1

        # for c in t:
        #     if charMap.get(c) == 0:
        #         return False
        #     charMap[c] = charMap.get(c, 0) - 1
        
        # return all(charMap.get(k, 0) == 0 for k in charMap)