class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
        print(m)
        
        for i in range(len(nums)):
            if target-nums[i] in m:
                return [i, m.get(target-nums[i])]
        return [0,0]
        