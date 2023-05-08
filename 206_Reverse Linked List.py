# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_list = []
        while head:
            num_list.append(head.val)
            head = head.next

        if not num_list:
            return None

        head = ListNode(val=num_list.pop())

        cur = head
        while num_list:
            cur.next = ListNode(val=num_list.pop())
            cur = cur.next
        
        return head
