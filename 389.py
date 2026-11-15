class Solution(object):
    def findTheDifference(self, s, t):
        sumi=0
        diff=0
        for i in t:
            sumi+=ord(i)-ord('a')
        for i in s:
            diff+=ord(i)-ord('a')

        return chr(sumi-diff+ord('a'))
        