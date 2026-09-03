class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
        
        for i in range(len(nums)):
            t = target - nums[i]
            if t in m and m[t] != i:
                return [i, m.get(t)]
        return [0,0]
        