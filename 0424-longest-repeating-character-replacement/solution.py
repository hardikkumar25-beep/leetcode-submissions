class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        count={}
        best=0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while (right-left+1)-max(count.values())>k:
                count[s[left]]-=1
                left+=1
            best = max(best, right - left + 1)
        return best
