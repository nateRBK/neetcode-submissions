# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #after grabbing the n-1 node, and swapping it to the 1th place,
        #the n-2 node is the new final element, which is then switched to 
        #after the old 2nd place.
        #so at every swap I am just grabbing the last element of the list
        #and inserting it after that element
        c = head
        while c.next and c.next.next: 
            end = newEnd = c
            while end.next:
                if not end.next.next:
                    newEnd = end
                end = end.next
            temp = c.next
            c.next = end
            end.next = temp
            newEnd.next = None
            c = c.next.next




