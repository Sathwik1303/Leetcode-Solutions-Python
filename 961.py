class Solution(object):
    def repeatedNTimes(self, nums):
        seen={}
        for i in nums:
            if i in seen:
                return i
            seen[i]=1
        