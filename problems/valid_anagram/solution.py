class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqS={}
        freqT={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            freqS[s[i]]=freqS.get(s[i],0)+1
            freqT[t[i]]=freqT.get(t[i],0)+1
        return freqS==freqT
        