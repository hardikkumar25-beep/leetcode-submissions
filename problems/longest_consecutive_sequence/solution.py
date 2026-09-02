class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen=set(nums)
        longest=0
        for num in seen:
            if not nums:
                return 0
            if num-1 in seen:
                continue
            current =num
            length=1
            while current+1 in seen:
                current+=1
                length+=1
            longest=max(longest,length)
        return longest
