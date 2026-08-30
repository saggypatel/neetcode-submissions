public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> list = new HashSet<int>();

        foreach (var num in nums)
        {
            if(list.Contains(num)) {
                return true;
            }
            list.Add(num);
        }

        return false;
    }
}
