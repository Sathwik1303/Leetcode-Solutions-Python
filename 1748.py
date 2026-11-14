class Solution(object):
    def sumOfUnique(self, nums):
        seen={}
        for i in nums:
            seen[i]=seen.get(i,0) +1
        sum=0
        for key,value in seen.items():
            if value==1:
                sum+=key
        return sum
        