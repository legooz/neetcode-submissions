# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp_head = head
        original_head = head

        while head is not None:
            arr.append(head.val)
            head = head.next
        
        for num in reversed(arr):
            temp_head.val = num
            temp_head = temp_head.next


        return original_head
