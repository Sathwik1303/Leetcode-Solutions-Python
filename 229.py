class Solution(object):
    def majorityElement(self, nums):
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0) +1
        threshold=len(nums)/3
        ans=[]
        for key,value in seen.items():
            if (value>threshold):
                ans.append(key)
        return ans