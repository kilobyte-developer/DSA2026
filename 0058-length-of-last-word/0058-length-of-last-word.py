class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        for i in range(n-1,-1,-1):
            if s[i] != " ":
                count+=1
                if s[i-1] == " ":
                    break

        return count