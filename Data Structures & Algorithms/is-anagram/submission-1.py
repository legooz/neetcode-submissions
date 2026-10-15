class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}
        for ch in s:
            s_counts[ch] = s_counts.get(ch, 0) + 1

        for ch in t:
            t_counts[ch] = t_counts.get(ch, 0) + 1

        if(t_counts != s_counts):
            return False


        return True
            