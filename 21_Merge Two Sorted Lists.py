# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        while list1 or list2:
            cur.next = ListNode()
            cur = cur.next
            if not list1:
                cur.val = list2.val
                list2 = list2.next
            elif not list2:
                cur.val = list1.val
                list1 = list1.next
            elif list1.val <= list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
        return head.next
