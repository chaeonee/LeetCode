# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            tmp = cur
            cur = cur.next
            tmp.next = None

        start, end = 0, len(arr)-1
        while start < end:
            arr[start].next = arr[end]
            start += 1
            end -= 1
        
        start, end = 1, len(arr) - 1
        while start < end:
            arr[end].next = arr[start]
            start += 1
            end -= 1
        
        return head
