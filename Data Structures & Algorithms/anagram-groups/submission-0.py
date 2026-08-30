class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in res:
                res[s_sorted].append(s)
            else:
                res[s_sorted] = [s]
        return list(res.values())
