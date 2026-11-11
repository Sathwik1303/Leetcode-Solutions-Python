class Solution(object):
    def singleNumber(self, nums):
        ans={}
        for i in nums:
            ans[i]=ans.get(i,0) +1
        for key,value in ans.items():
            if (value==1):
                return key
        