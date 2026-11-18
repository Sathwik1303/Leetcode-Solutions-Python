class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        nums.sort()
        diff=0
        for i in range(0,len(nums)-1):
            if diff<nums[i+1]-nums[i]:
                diff=nums[i+1]-nums[i]
        return diff
        