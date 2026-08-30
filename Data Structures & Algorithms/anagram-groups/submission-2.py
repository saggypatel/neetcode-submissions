class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rm = {}

        for s in strs:
            keyMap = [0] * 26
            for c in s:
                idx = ord(c) % 26
                keyMap[idx] += 1
            key = str(keyMap)
            if(key in rm):
                rm[key].append(s)
            else:
                rm[key] = [s]
        # print(rm)
        return list(rm.values())