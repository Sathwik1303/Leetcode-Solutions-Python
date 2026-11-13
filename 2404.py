class Solution(object):
    def mostFrequentEven(self, nums):
        seen={}
        for i in nums:
            if (i%2==0):
                seen[i]=seen.get(i,0)+1
        if not seen:
            return -1
        ans=[]
        bestval=None
        for key,value in seen.items():
            if (value>bestval):
                bestval=value
        for key,value in seen.items():
            if (value==bestval):
                ans.append(key)
        return (min(ans))

        