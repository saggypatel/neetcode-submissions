public class Solution {
    public bool IsAnagram(string s, string t) {
        var map = new Dictionary<char, int>();
        
        int currentValue;
        foreach(var c in s) {
            if(map.ContainsKey(c))
            {
                map[c]++;
            }
            else 
            {
                map.Add(c, 1);
            }
        }

        foreach(var c in t) {
            if(!map.ContainsKey(c))
            {
                return false;
            }
            else 
            {
                map[c]--;
            }
        }

        return map.Values.All(v => v==0);
    }
}
