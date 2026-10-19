# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # Node reference (pointer)
        curr = head # Node reference (pointer)
                                                        # None->[]->[]->[]->[]->None
        while curr: #while curr is not None equivalent
            nxt = curr.next
            curr.next = prev                            # None<-[curr]->[]->[]->[]->None
            prev = curr                                 # None<-[curr = prev]->[]->[]->[]->None
            curr = nxt                                  # None<-[prev]->[curr]->[]->[]->None


        return prev