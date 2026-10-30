class Solution(object):
    def modifiedList(self, nums, head):
        bad=set(nums)
        dummy=ListNode(0,head)
        curr=dummy
        while curr.next:
            if (curr.next.val in bad):
                curr.next=curr.next.next
            else:
                curr=curr.next
            
        return dummy.next