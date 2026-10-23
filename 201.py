class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        ans=0
        while (left!=right):
            left>>=1
            right>>=1
            ans+=1
        return (left<<ans)
        