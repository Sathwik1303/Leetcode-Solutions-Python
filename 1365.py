class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        ans = {}
        for i, x in enumerate(sorted_nums):
            if x not in ans:
                ans[x] = i
        result = []
        for x in nums:
            result.append(ans[x])
        return result