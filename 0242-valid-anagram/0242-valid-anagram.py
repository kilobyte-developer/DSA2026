class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        mp = {}
        mp2 = {}

        for char in s:
            if char in mp:
                mp[char] +=1
            else:
                mp[char] = 1
        
        for char2 in t:
            if char2 in mp2:
                mp2[char2] +=1
            else:
                mp2[char2] = 1

        return mp==mp2
        