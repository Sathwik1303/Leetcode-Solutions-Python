class Solution(object):
    def uniqueOccurrences(self, arr):
        seen={}
        for i in arr:
            seen[i]=seen.get(i,0)+1
        count=set()
        for key,value in seen.items():
            count.add(value)
        return (len(count)==len(seen))
        