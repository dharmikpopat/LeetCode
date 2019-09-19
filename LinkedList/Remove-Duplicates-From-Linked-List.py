class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dict_ = {}
        p = head
        dict_[p.val] = p.val
        
        while p.next is not None:
            if p.next.val in dict_.values():
                p.next = p.next.next
            else:
                dict_[p.next.val] = p.next.val
                p = p.next
                
        return head
    