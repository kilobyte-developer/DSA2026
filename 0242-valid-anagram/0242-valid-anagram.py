class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mp1 = {}
        mp2 = {}

        if len(s)!=len(t):
            return False

        for char1 in s:
            mp1[char1] = mp1.get(char1,0)+1
        
        for char2 in t:
            mp2[char2] = mp2.get(char2,0)+1

        return mp1==mp2