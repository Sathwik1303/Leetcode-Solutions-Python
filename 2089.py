class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        low=0
        check=0
        for i in nums:
            if (i<target):
                low+=1
            elif (i==target):
                check+=1
        ans=[]
        for i in range(0,check):
            ans.append(low+i)
        return ans        