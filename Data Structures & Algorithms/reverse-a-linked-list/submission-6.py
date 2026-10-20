# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def recursive(self, head:Optional[ListNode], prev, curr) -> Optional[ListNode]:
    if curr is None: #curr = 1
        print("base case, prev =", prev)
        return prev

    nxt = curr.next #nxt = 2
    curr.next = prev #  None <- curr = 1
    prev = curr # None <- curr = 1 = prev
    curr = nxt # None <- prev = 1 <- curr = 2
    return recursive(self, head, prev, curr)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head


        return recursive(self, head, prev, curr)





        # prev = None # Node reference (pointer)
        # curr = head # Node reference (pointer)
        #                                                 # None->[]->[]->[]->[]->None
        # while curr: #while curr is not None equivalent
        #     nxt = curr.next
        #     curr.next = prev                            # None<-[curr]->[]->[]->[]->None
        #     prev = curr                                 # None<-[curr = prev]->[]->[]->[]->None
        #     curr = nxt                                  # None<-[prev]->[curr]->[]->[]->None


        # return prev

