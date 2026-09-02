class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -s for s in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 != s2:
                diff = -abs(s1-s2)
                heapq.heappush(stones, diff)
        
        return -stones[0] if stones else 0