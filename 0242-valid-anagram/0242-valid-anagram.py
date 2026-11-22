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
            mp[char] = mp.get(char,0)+1

        for char2 in t:
            mp2[char2] = mp2.get(char2,0)+1

        return mp==mp2
        