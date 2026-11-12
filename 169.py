class Solution(object):
    def majorityElement(self, nums):
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0)+1
        bestval=None
        for key,value in seen.items():
            if (value>bestval):
                bestval=value
                bestkey=key
        return bestkey
        