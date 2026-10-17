class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 = circular
        # 1 = square
        # students = queue
        # sandwiches = stack

        cur = Node(students[0])
        head = cur
        for student in students[1:]:
            node = Node(student)
            cur.next = node
            cur = node
        tail = cur
        

        cur = head
        rejection_count = 0
        while sandwiches:
            sandwich = sandwiches[0]
            if(rejection_count >= len(sandwiches)):
                break

            if(head.val == sandwich):
                sandwiches.pop(0)
                cur = cur.next
                head = cur
                rejection_count = 0
            elif(len(sandwiches) == 1 and head.val != sandwich):
                break
            else:
                rejection_count += 1
                head = cur.next
                cur.next = None
                tail.next = cur
                tail = cur
                cur = head


        return len(sandwiches)



