class Solution(object):
    def hammingWeight(self, n):
        digit=0
        count=0
        while (n>0) :
            digit=n%2
            n=n/2
            if (digit==1):
                count+=1
        return count