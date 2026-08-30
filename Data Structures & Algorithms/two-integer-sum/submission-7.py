class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
        # print(m)
        
        for i in range(len(nums)):
            t = target - nums[i]
            if t in m and m[t] != i:
                print("looking for ", t, " and found", m.get(t))
                return [i, m.get(t)]
        return [0,0]
        