class Solution(object):
    def detectCycle(self, head):
        seen=set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head=head.next
        return head