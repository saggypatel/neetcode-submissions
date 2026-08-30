class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = {}
        for c in s:
            charMap[c] = charMap.get(c, 0) + 1

        for c in t:
            if charMap.get(c) == 0:
                return False
            charMap[c] = charMap.get(c, 0) - 1

        
        return all(charMap.get(k, 0) == 0 for k in charMap)